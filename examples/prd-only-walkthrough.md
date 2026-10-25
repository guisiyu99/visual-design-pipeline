# PRD-only 示例：从零开始

1. 用户提供 [虚构 PRD](sample-prd.md)，没有参考或设计稿。
2. Agent 提取门店店长/运营角色、订单查询与异常处理流程；推荐“订单列表”和“订单详情 + 异常状态”作为样板。
3. Agent 寻找 2–3 种真实视觉参考，由用户确认一个方向。
4. Agent 提取带来源及不确定项的 design-spec.md。
5. Agent 生成 Stitch/Figma 提示词；有权限则操作，否则要求返回截图或链接。
6. Agent 评审样板并处理 P0/P1，用户确认后才固化 design.md。
7. Agent 基于规范生成剩余页面，并更新 review-log 与 lessons。

**注意**：这是流程说明，不代表已在外部工具执行。
