# 3. EventAggregator 事件聚合（跨模块通信）

> 片段来自 Prism-Samples-Wpf（14/15）。

## 3.1 基本发布/订阅

发布/订阅模式，默认弱引用，避免内存泄漏。自定义事件继承 `PubSubEvent<T>`（示例 14）：

```csharp
// 1) 定义事件（共享/Core 项目）
public class MessageSentEvent : PubSubEvent<string> { }

// 2) 发布方（ModuleA）
IEventAggregator _ea;
public MessageViewModel(IEventAggregator ea) { _ea = ea; SendMessageCommand = new DelegateCommand(SendMessage); }
private void SendMessage() => _ea.GetEvent<MessageSentEvent>().Publish(Message);

// 3) 订阅方（ModuleB）
public MessageListViewModel(IEventAggregator ea)
{
    _ea = ea;
    Messages = new ObservableCollection<string>();
    _ea.GetEvent<MessageSentEvent>().Subscribe(MessageReceived);
}
private void MessageReceived(string message) => Messages.Add(message);
```

## 3.2 订阅高级选项：线程与过滤（示例 15）

```csharp
_ea.GetEvent<MessageSentEvent>().Subscribe(
    MessageReceived,
    ThreadOption.PublisherThread,     // 回调线程
    keepSubscriberReferenceAlive: false,
    filter: msg => msg.Contains("Brian")   // 仅接收满足条件的消息
);
```

| `ThreadOption` | 含义 |
|---|---|
| `PublisherThread` | 在发布者线程执行（默认） |
| `UIThread` | 切回 UI 线程（WPF 最常用，避免跨线程访问控件） |
| `BackgroundThread` | 线程池执行 |

> 取消订阅：`_ea.GetEvent<MessageSentEvent>().Unsubscribe(MessageReceived)`。若用 `keepSubscriberReferenceAlive:true`，必须显式 `Unsubscribe` 否则泄漏。与用户的 `WeakEventManager` 解耦模式可互补使用。

## 3.3 与 WeakEventManager 的关系

- `EventAggregator` 默认使用弱引用订阅者，适合跨模块、松耦合的语义化事件（`PubSubEvent<T>` 携带业务负载）。
- `WeakEventManager`（.NET 原生）适合同一进程内、基于事件名的轻量解耦绑定，避免事件导致的目标不被 GC。
- 两者都解决「订阅者泄漏」问题；Prism 项目中跨模块通信优先用 `EventAggregator`，VM 内部对具体事件源的弱绑定可用 `WeakEventManager`。
