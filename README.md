# pairwise-skeet-hit-register

## 领域

游戏、图形与多媒体

## 主题

飞碟射击命中登记

## 说明

靶机服务端排程、弹丸锥判定与命中单一裁决。

初始状态下 `gameplay/skeet_hit_register.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
