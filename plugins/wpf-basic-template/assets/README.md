# __APP_NAME__

基于 [Prism 9](https://github.com/PrismLibrary/Prism) + Material Design 5（默认 MD3 主题）+ [CommunityToolkit.Mvvm](https://github.com/CommunityToolkit/dotnet) 的标准 WPF 桌面应用示例。

> 本说明文档为模板生成，不含任何敏感信息（无个人身份、凭证、内网地址）。请按需补全项目实际说明。

## 技术栈

| 类别 | 选型 |
|---|---|
| 框架 | .NET（WPF，`netX.0-windows`） |
| MVVM / 组合 | Prism.Wpf + Prism.DryIoc |
| UI 主题 | MaterialDesignThemes（MD3）+ MahApps.Metro（MetroWindow） |
| 源代码生成 | CommunityToolkit.Mvvm（`[ObservableProperty]` / `[RelayCommand]`） |
| 包管理 | 中央包管理（CPM，`Directory.Packages.props`） |
| 解决方案 | slnx 格式（`__APP_NAME__.slnx`） |
| 日志 | Serilog（文件按天滚动） |

## 目录结构

```
__APP_NAME__/
├─ __APP_NAME__.slnx          # slnx 解决方案
├─ Directory.Packages.props   # CPM 集中版本
├─ Directory.Build.props      # 公共编译属性
├─ nuget.config               # NuGet 源（仅官方 nuget.org）
├─ .gitignore
├─ README.md                  # 本文档
├─ LICENSE                    # MIT 协议
└─ src/
   ├─ __APP_NAME__/               # WPF 应用（组合根）
   │  ├─ Views/  ViewModels/
   ├─ __APP_NAME__.Domain/        # 领域模型
   ├─ __APP_NAME__.Application/   # 契约（接口）
   └─ __APP_NAME__.Infrastructure/ # 实现
```

依赖方向：`__APP_NAME__` → Infrastructure → Application → Domain。

## 构建与运行

```bash
dotnet restore
dotnet build --no-restore
dotnet run --project src/__APP_NAME__/__APP_NAME__.csproj
```

要求：`dotnet build` 结果 **0 错误 0 警告**。

## 约定速查

- 包版本集中在 `Directory.Packages.props`，禁止 `dotnet add package`。
- ViewModel 属性一律用 C# 13 分部属性（`[ObservableProperty]`），禁私有字段老写法。
- 所有源文件纯 UTF-8 无 BOM。
- 全局异常由 App 三钩子统一收口，ViewModel 内不 try-catch。

## 许可证

详见 [LICENSE](LICENSE)（MIT）。
