# 4. Regions 区域与 Modules 模块化

> 片段来自 Prism-Samples-Wpf（02/03/04/05/06/07/14/16）。

## 4.1 Regions 区域

在 Shell/View 中声明命名区域，运行时动态注入视图。

```xml
<ContentControl prism:RegionManager.RegionName="ContentRegion" />   <!-- 单视图 -->
<ItemsControl  prism:RegionManager.RegionName="TabRegion" />        <!-- 多视图列表 -->
```

| 注入方式 | 代码示例 | 示例 |
|---|---|---|
| View Discovery | `regionManager.RegisterViewWithRegion("Region", typeof(ViewA));` | 04 |
| View Injection | `var v = region.Add(view); region.Activate(v);` | 05 |
| Activation | `region.Activate(viewA); region.Deactivate(viewB);` | 06 |
| 自定义适配器 | 继承 `RegionAdapterBase<T>` 并注册 | 03 |

### 自定义区域适配器（示例 03：让 StackPanel 支持 Region）

```csharp
public class StackPanelRegionAdapter : RegionAdapterBase<StackPanel>
{
    public StackPanelRegionAdapter(IRegionBehaviorFactory f) : base(f) { }

    protected override void Adapt(IRegion region, StackPanel target)
    {
        region.Views.CollectionChanged += (s, e) =>
        {
            if (e.Action == NotifyCollectionChangedAction.Add)
                foreach (FrameworkElement el in e.NewItems)
                    target.Children.Add(el);
            // 处理 Remove ...
        };
    }
    protected override IRegion CreateRegion() => new AllActiveRegion();   // 全部激活
}
// 注册：在 App 中重写 ConfigureDefaultRegionBehaviors 或 App.xaml 合并字典里注册适配器
```

## 4.2 Modules 模块化

把功能拆成 `IModule`（独立程序集、可插拔）。完整示例（14 ModuleA 用 Discovery 把视图注册到区域）：

```csharp
public class ModuleAModule : IModule
{
    public void OnInitialized(IContainerProvider containerProvider)
    {
        var regionManager = containerProvider.Resolve<IRegionManager>();
        regionManager.RegisterViewWithRegion("LeftRegion", typeof(MessageView));
    }
    public void RegisterTypes(IContainerRegistry containerRegistry) { /* 注册本模块服务 */ }
}
```

### 四种模块加载方式（示例 07）

| 方式 | 代码 / 配置 | 示例 |
|---|---|---|
| 代码 | `ConfigureModuleCatalog` → `moduleCatalog.AddModule<ModuleAModule>()` | 07-Code |
| App.config | `<modules><module assemblyFile=".." moduleType=".." moduleName="ModuleA"/></modules>` | 07-AppConfig |
| 目录 | `moduleCatalog.AddModuleDirectory("Modules");` | 07-Directory |
| 手动 | `containerProvider.Resolve<IModuleManager>().LoadModule("ModuleA");` | 07-LoadManual |

> 模块依赖：`moduleCatalog.AddModule<ModuleB>().AddModule<ModuleA>()` 表示 B 依赖 A（先加载 A）。模块适合把大型系统按业务拆分（如用户的上料/视觉/运控模块），主壳只负责组合。

## 4.3 Region 四种内容填充方式对照

| 方式 | 是否有状态/历史 | 适用 |
|---|---|---|
| View Discovery | 自动注入，无导航历史 | 固定布局（如工具栏、状态栏） |
| View Injection | 手动增删，无历史 | 动态增删视图 |
| View Activation | 激活/停用，无历史 | 同一区域多视图切换显示 |
| Region Navigation | 有状态、有 Journal 历史 | 主内容区「页面」式切换、传参、确认离开 |
