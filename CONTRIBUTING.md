# Contributing to AI Robot 实验记录

感谢你对本项目的关注！这是一个 AI 机器人课程的学习实验仓库，欢迎提交改进建议。

## 如何贡献

### 报告问题

如果你发现实验代码有 Bug、文档有错误、或截图缺失/过时，请：

1. 在 [Issues](https://github.com/ctrlCvsix/ai-robot-wangjiaxiong/issues) 中创建新 Issue
2. 描述问题所在（周次 + 文件名）
3. 提供复现步骤或截图

### 提交改进

1. **Fork** 本仓库
2. 创建功能分支：`git checkout -b fix/weekXX-description`
3. 提交更改：`git commit -m "fix: update WeekXX README with corrected steps"`
4. 推送到你的 Fork：`git push origin fix/weekXX-description`
5. 提交 **Pull Request** 到本仓库的 `main` 分支

### 命名规范

- 分支名：`fix/short-description` 或 `feat/short-description`
- 提交信息：使用中文或英文，简洁描述改动内容
- 示例：`docs: 补充 Week05 逆运动学公式推导` 或 `fix: 修复 Week09 A* 算法路径重复问题`

## 代码风格

- Python 代码遵循 PEP 8 规范
- Markdown 文件使用中文编写
- 图片请压缩后放入对应周的 `img/` 目录
- Docker 相关文件确保 `docker compose` 语法兼容 v2

## 许可证

提交贡献即表示你同意将代码以 [MIT License](./LICENSE) 授权。
