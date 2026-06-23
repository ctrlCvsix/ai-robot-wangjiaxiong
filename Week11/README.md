# Week 11 — GitHub Pages 网页部署实践

## 实验目标

将课程作业仓库部署为 GitHub Pages 静态网站，掌握 Git 版本管理与自动化部署流程，使实验报告可在浏览器中直接访问。

## 实验环境

| 组件 | 说明 |
|------|------|
| 版本管理 | Git + GitHub |
| 部署平台 | GitHub Pages |
| 配置格式 | YAML (_config.yml) |
| 内容格式 | Markdown |
| 容器环境 | Docker（用于本地预览） |

## 目录结构

```
Week11/
├── README.md                # 本报告
├── 514.png                  # GitHub Pages 部署成功截图
├── 514_2.png                # 网页访问验证截图
├── docker_advanced.png      # Docker 高级操作截图
└── github_pages_prepare.png # Pages 配置准备截图
```

## 实验步骤

### 1. 配置 GitHub Pages

在仓库 Settings → Pages 中选择部署分支（main）和根目录，GitHub 会自动触发构建。

### 2. 准备部署内容

确保仓库根目录包含入口文件（README.md 或 index.html），并配置 `_config.yml`：

```yaml
theme: jekyll-theme-minimal
title: AI Robot 实验导航
description: 课程实验 · 仿真模拟 · 视觉记录
```

### 3. 推送并验证

提交更改并推送到 GitHub，等待 Pages 构建完成后通过 `https://<username>.github.io/<repo>` 访问。

### 4. Docker 环境验证

在 Docker 容器中本地预览 Pages 效果，确保部署前内容正确。

## 关键命令

```bash
# 初始化仓库并推送
git init
git add .
git commit -m "Deploy GitHub Pages"
git branch -M main
git remote add origin <repo-url>
git push -u origin main

# Docker 本地预览
docker run --rm -p 4000:4000 -v $(pwd):/site bretfisher/jekyll-serve
```

## 实验证据

### GitHub Pages 部署成功

<img src="514.png" width="800" alt="GitHub Pages 部署成功">

*GitHub Pages 构建成功，网站可公开访问*

### 网页访问验证

<img src="514_2.png" width="800" alt="网页访问验证">

*浏览器中验证部署结果，所有页面正常渲染*

### Pages 配置准备

<img src="github_pages_prepare.png" width="800" alt="Pages 配置准备">

*仓库 Settings 中的 Pages 配置界面*

### Docker 环境准备

<img src="docker_advanced.png" width="800" alt="Docker 高级操作">

*Docker 容器中本地预览，验证部署效果*

## 遇到的问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| Pages 构建失败 | Jekyll 主题未正确配置或 `_config.yml` 格式错误 | 检查 YAML 缩进，确认 theme 名称与 GitHub 支持列表一致 |
| 图片 404 | 路径使用了绝对路径而非相对路径 | 统一使用相对路径 `./images/xxx.png` 引用资源 |
| 本地预览与线上不一致 | Jekyll 版本差异 | 使用 GitHub Pages 官方 Docker 镜像确保环境一致 |
| 构建速度慢 | 仓库过大包含大量二进制文件 | 使用 `.gitignore` 排除不必要的生成文件 |

## 总结与反思

### 核心收获

1. **自动化部署流程**：GitHub Pages 实现了 push → build → deploy 全自动，只需专注内容编写
2. **Git 版本管理**：通过 `.gitignore`、commit message 规范、分支策略，团队协作更高效
3. **静态站点优势**：Markdown → HTML 自动转换，无需后端服务器，维护成本低

### 延伸思考

GitHub Pages 不仅是课程作业的展示工具，更是建立个人技术品牌的重要方式：
- 可扩展为个人博客（Jekyll/Hugo 等静态站点生成器）
- 结合 GitHub Actions 可实现更复杂的自动化发布
- 自定义域名可提升专业度

---

[返回实验导航](../README.md)
