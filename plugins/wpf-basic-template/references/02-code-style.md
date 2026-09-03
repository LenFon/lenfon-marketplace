# 代码风格强制约定

## 分部属性（强制）：一切 `[ObservableProperty]` 必须写成分部属性

**凡标注 `[ObservableProperty]` 的可通知属性，一律声明为 C# 13 分部属性 `public partial T Xxx { get; set; }`。「私有字段 + 生成器造属性」的旧写法全面禁止，`partial` 关键字不可省略。**

```csharp
// 正确 —— [ObservableProperty] + 分部属性
[ObservableProperty]
public partial string Title { get; set; } = "默认值";

// 错误 —— 禁止：私有字段老写法
[ObservableProperty]
private string _title = "默认值";

// 错误 —— 禁止：非分部属性（缺 partial）
[ObservableProperty]
public string Title { get; set; } = "默认值";
```

规则细化：

- **不得手工维护 `_xxx` 支持字段**；属性初始化器可用（CommunityToolkit.Mvvm 8.4.2 + net10 实测）。
- 访问修饰符按场景取 `public`（数据绑定所需）等，但 `partial` 必须保留。
- `[NotifyCanExecuteChangedFor(nameof(XxxCommand))]`、`[NotifyPropertyChangedFor(nameof(Yyy))]` 等特性照常叠加在分部属性上，行为不变。
- **变更回调一律用强类型 partial 方法** `partial void OnXxxChanged(T value)`，不再依赖 `On<字段名>Changed` 命名约定；另有 `OnXxxChanging(T value)`、`OnXxxChanged(T oldValue, T newValue)` 重载可选。
- 纯语言层（非 MVVM）同样可用：定义声明 `public partial bool IsToday { get; }` 与实现声明 `public partial bool IsToday => ...;` 分置两个 partial 文件。

### 生成后自检（强制）

写完含 `[ObservableProperty]` 的代码后**必须扫描校验**：任一 `[ObservableProperty]` 之后的声明若不含 `partial`、或落在 `private` 字段上，即为违规，改正后复校至输出 OK。

```bash
python - <<'EOF'
import pathlib, re
attr = re.compile(r'^\s*\[ObservableProperty\]\s*$')
bad = []
for p in pathlib.Path('src').rglob('*.cs'):
    lines = p.read_text(encoding='utf-8').splitlines()
    for i, ln in enumerate(lines):
        if not attr.match(ln):
            continue
        # 跳过紧随其后的其它特性行，取真正的声明行
        j = i + 1
        while j < len(lines) and lines[j].strip().startswith('['):
            j += 1
        decl = lines[j] if j < len(lines) else ''
        if 'partial' not in decl or re.search(r'\bprivate\b', decl):
            bad.append(f"{p}:{j + 1}: {decl.strip()}")
print('VIOLATIONS:' if bad else 'OK: 全部 [ObservableProperty] 均为分部属性')
print('\n'.join(bad))
EOF
```

> 该脚本在解决方案根执行（扫描 `src/` 下全部 `.cs`）。VM 常与 `.Design.cs` 成对出现，两者都在扫描范围内，均须合规。

## XML 文档注释格式（强制，多行）

**生成的所有 `.cs` 代码，XML 文档注释（`///`）一律展开成多行，禁止把 `summary`/参数/返回值压成单行。**

```csharp
// 正确 —— 每个标签独立成行
/// <summary>
/// 计算指定区间内的消息总数。
/// </summary>
/// <param name="from">起始时间（含）。</param>
/// <param name="to">结束时间（不含）。</param>
/// <returns>匹配的消息条数。</returns>
public int Count(DateTime from, DateTime to) => ...;

// 错误 —— 禁止单行压写
/// <summary>计算指定区间内的消息总数。</summary>
```

- 凡有公开类型 / 成员，先用多行 `/// <summary>`；含参数或返回值再补 `/// <param>` / `/// <returns>`，各占一行。
- 该约束仅针对生成的新代码；改造既有文件时，若其已是单行注释且功能正常，可不强制展开（避免无意义改动）。

## 单行注释位置（强制，置于变量/字段上方）

**解释性单行注释（`//`）若用于说明某个【变量】或【字段】，一律写在该变量/字段声明的【上一行】，不得写成行尾跟随注释（trailing comment）。**

```csharp
// 正确 —— 注释在字段上方
// 保护 _isShowingDialog 的检查与赋值（三钩子可能并发）
private static readonly Lock ShowDialogLock = new();

// 错误 —— 禁止行尾跟随
private static readonly Lock ShowDialogLock = new(); // 保护 _isShowingDialog 的检查与赋值（三钩子可能并发）
```

- 适用范围：变量声明、类字段（`readonly` 字段、静态字段、实例字段等）的 `//` 解释性注释，统一前置。
- 方法体语句级注释（如 `e.Handled = true;` 上方的说明）不在本强约束范围内，可灵活前置或行尾；默认仍偏好上方以保持统一风格。
- 例外（可保留行尾）：预处理器配对标记（如 `#endif // XXX`）本身允许跟随；确实只服务于本行、移动后反而割裂可读性的极短标注——默认仍以上方为准。
- 该约束针对生成的新代码；改造既有文件时，若其行尾注释功能正常且移动收益不大，可不强制改动（避免无意义 churn）。

## 优先使用 var 定义变量（强制）

**局部变量声明，只要初始化器能明确推断类型，一律用 `var`；不得显式写出本可由编译器推断的类型。**

```csharp
// 正确
var list    = new List<MessageItem>();
var item    = Container.Resolve<MainView>();
var message = $"异常：{ex.Message}";
var ex      = e.ExceptionObject as Exception ?? new Exception("未知错误");

// 错误 —— 类型已由 RHS 明确，不必写死
List<MessageItem> list = new();
MainView mv = Container.Resolve<MainView>();
```

- 适用：右侧为 `new`、显式转换、已知返回类型的方法调用、字符串插值/拼接等，类型推断直观的场景。
- 例外（保留显式类型）：① lambda 无目标类型无法推断（`Action show = () => { ... };` 不能写 `var`）；② 数值字面量需特定类型（`long n = 123;` 写 `var` 会推断成 `int`）；③ 需强调接口/基类而非具体实现（如 `IMessageService svc = new MessageService();` 凸显契约）；④ 右侧类型不直观、显式写出更利于可读性时。
- 字段级声明：net10 下字段可用 `var` 配合 `new()` 初始化器（`private static readonly Lock Locker = new();` 本就如此）；需显式类型或 `= null!` 占位的字段维持原样。
- 该约束针对生成的新代码；改造既有文件时，若显式类型不影响可读性且改动收益不大，可不强制改（避免无意义 churn）。

## 线程锁

线程同步锁一律用 `System.Threading.Lock`（net9+）：`private static readonly Lock X = new();`，`lock (X)` 写法不变，不用裸 `object` 当锁。
