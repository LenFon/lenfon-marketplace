# 编译验证（必须 0 错通过）

**生成项目后，必须实际跑通编译；只要存在编译错误，就进入「定位 → 修复 → 复编」循环，直到 0 错误为止。绝不中途交付「大概能编过」的产物。**

直接用 .NET SDK 还原包并编译生成的项目进行验证，无需任何额外绕行手段。**Git Bash / PowerShell 宿主下必须带 env 前缀**（`HOME` 用 Windows 反斜杠路径），否则首次 restore 必报 `Value cannot be null. (Parameter 'path1')`（根因见 `04-pitfalls.md`）：

```bash
env APPDATA='C:\Users\<用户>\AppData\Roaming' HOME='C:\Users\<用户>' PROGRAMFILES='C:\Program Files' dotnet restore
env APPDATA='C:\Users\<用户>\AppData\Roaming' HOME='C:\Users\<用户>' PROGRAMFILES='C:\Program Files' dotnet build --no-restore
```

- 报错即修：逐条读错误（CSxxxx / MCxxxx / 警告升错误），定位文件与行号，修复后**重新完整构建**验证，不得只修不复编。
- 反复失败要收敛：同一错误连续两轮未过，先停止盲目改、回到根因（命名空间、引用、CPM 版本、WPF 引导、XML 注释/命名空间带 `;assembly=` 等本技能坑位），必要时缩小范围（单项目 `dotnet build <csproj>`）隔离问题，再继续。
- 验收门槛：**0 错误**。警告原则上清零（本技能模板目标是 0 错 0 警）；确属第三方/工具链无害警告且无法消除的，需在交付说明里点名，不可默认忽略。
- 交付前告知用户：本沙箱无法完整运行 WPF，最终运行验证在 VS 中做；但「能编译到 0 错 0 警」必须由本技能在本机用 .NET SDK 验证完成。

## XAML 侧验证

XAML 由 MarkupCompile 处理，只要不报 MC 错、且 `obj/**/App.g.cs`、`Views/Shell.g.cs`、`Views/MainView.g.cs` 已产出，即说明 XAML 语法与 xmlns 类型引用通过。`dotnet build` 一次即覆盖 C# 与 XAML 两侧，无需拆分单独验证。
