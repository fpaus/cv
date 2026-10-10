# Fabrizio Dante Pauselli's CV

- Phone: +54 9 11 6975 9207
- Email: [fabriziopauselli@gmail.com](mailto:fabriziopauselli@gmail.com)
- Location: Buenos Aires, Argentina
- Website: [fpaus.github.iocv](https://fpaus.github.io/cv/)
- LinkedIn: [fabrizio-dante-pauselli-917365120](https://linkedin.com/in/fabrizio-dante-pauselli-917365120)
- GitHub: [fpaus](https://github.com/fpaus)


# Summary
Software Architect and Tech Lead with 10+ years in software engineering. I built and headed the Architecture & Cloud Infrastructure department of a remittance fintech (6 senior engineers, 500+ Azure resources under Terraform). Today I lead two teams (7 people) on a .NET / Angular / Azure platform built with .NET Aspire, and I designed the AI-assisted way they work: agent pipelines for code review and QA, an autonomous bug sweep, a LiteLLM gateway, MCP servers and Claude Code skills, all held to the line by architecture tests and spec-driven development.

# Skills
**Backend:** C#, .NET 8/10, ASP.NET Core Web API, Entity Framework Core, .NET Aspire, Hangfire, Native AOT, Avalonia, Node.js (NestJS), Python, Go

**AI Engineering:** LLM gateway and spend tracking (LiteLLM), Model Context Protocol (MCP), AI coding agents (Claude Code, opencode, Antigravity), multi-agent workflows and skills, agent context and memory, AI-assisted code review and QA, local LLMs (Ollama), on-device speech (sherpa-onnx), AI guardrails

**Cloud & DevOps:** Azure (App Service, Functions, SQL, Key Vault, Entra ID, managed identities, private endpoints, Application Insights), Terraform, GitHub Actions, Docker, OpenTelemetry

**Architecture & Quality:** Clean Architecture, SOLID, CQRS, ADRs, architecture tests, ATDD, spec-driven development (OpenSpec), architecture-as-code (LikeC4), Testcontainers, Playwright, mutation testing (Stryker), stacked PRs, code review

**Frontend:** Angular, TypeScript, React, Next.js

**Data:** SQL Server, PostgreSQL, SQLite, query optimization

**Leadership:** People management, performance evaluations, onboarding, mentoring, iteration and capacity planning, technical roadmaps, stakeholder demos

# Experience
## **Architect / Technical Lead**, Craft-Labs -- Buenos Aires, AR

Mar 2026 – present

- Lead two engineering teams (7 people) that ship in 2-week iterations: I run capacity planning, iteration demos to stakeholders and the technical roadmap.

- Own the architecture and delivery of the company's operations platform (SOWs, allocations, invoicing, performance feedback, compensation; ~20 screens, 8 roles) on .NET, Angular, Azure Functions and SQL Server, orchestrated with .NET Aspire.

- Designed the AI-assisted code review process the teams run on every pull request: 5 agents in parallel (checks, standards, spec, tests, security) that handle stacked chains of up to 13 PRs and enforce the coding and architecture standards I define.

- Created a repeatable autonomous bug-sweep process with parallel coding agents (12 hunt rounds, ~9 fix agents per run). First run: 65 pull requests and 74 bugs traced to the change that introduced them, in 7.5 unattended hours.

- Built the AI-assisted regression QA process (plan, run, triage): agents derive the test cases from merged PRs, run them in Playwright with video evidence and file the bugs. First pass: 56 cases from 90 PRs, 10 bugs reported.

- Built the platform's quality system: ratcheted architecture tests, mutation testing (Stryker), analyzer and lint ratchets, and suites of ~3,000 unit, 1,600 integration (Testcontainers) and 4,400 UI tests. Cut CI spend with on-demand checks and local integration runs from 22 to 3 minutes.

- Hardened the platform's Azure footprint end to end: identity-based access between services, closed network exposure and restricted SQL Server access.

- Designed and built the company-wide LLM gateway (LiteLLM) for engineers and for products with agentic capabilities, local and hosted models, as a production-grade Azure deployment with spend tracking per team and model: Terraform (24 resources), App Service, private PostgreSQL, Key Vault, Entra ID, Application Insights, budget alerts.

- Built the teams' agentic development toolkit: 30+ Claude Code skills for the whole cycle (spec, change, review, QA, release, daily reports) plus a shared context and memory layer across AI coding agents, so every engineer works the same way with AI.

- Own people development: weekly performance evaluations for all 7 team members, the onboarding plan that brought 5 hires up to speed in 2026, and the company-wide performance feedback cycle as product owner of that module.



## **Lead Architect**, Remitee -- Buenos Aires, AR

Feb 2023 – Feb 2026

- Built and headed the Architecture & Cloud Infrastructure department of a cross-border remittance fintech: hired its 6 senior architects and cloud engineers (2 teams), ran their performance reviews and career development, and helped other teams hire.

- Led the project that brought 500+ Azure resources under Terraform, cutting provisioning from hours or days of manual work to under an hour.

- Led the split of a ~50-microservice monorepo into one repository per service and their migration from .NET Core 2 to .NET 6 and 8.



## **Technical Leader**, SoulIT -- Buenos Aires, AR

Feb 2022 – Feb 2023

- Led two concurrent delivery teams of 3–4 engineers each with Agile practices.



## **Software Architect (part-time)**, Independent Consulting -- Remote

Jan 2019 – present

- Architected a collections hub for a wholesale bank (2026) from client requirements to an approved design: LikeC4 model with 21 views, 7 ADRs and 19 recorded decisions on Spring, Kafka with outbox/inbox, Keycloak and OpenShift, sized for 5,000 TPS.



## **Software Developer · QA Analyst**, Public sector: ANSES, Ministries of Production and Labor -- Buenos Aires, AR

May 2015 – Sep 2019

- Development in Agile teams (2018–2019) after three years of manual and automated testing (2015–2018).



# Selected Projects
**Unified Workbench:** Agent-built product: a .NET / Avalonia desktop app plus MCP hosts (~37 tools) for daily reports, GitHub boards and effort analysis. I designed it (24 ADRs, LikeC4 model, architecture tests) and had parallel Claude Code subagents implement its ~380-issue backlog with token cost tracked per ticket; 960+ tests.

**Open source:** pnpm/pnpm#15724 (merged): fix for Windows `.cmd` shims broken by `%` in paths, in Rust and TypeScript with tests. microsoft/aspire#20652: SQL `WithRepl` failure on CRLF scripts.

# Teaching & Mentoring
## **Technical Instructor**, Coderhouse & EducacionIT -- Buenos Aires, AR

Jan 2023 – present

- Created and teach the "Web APIs with .NET" course at EducacionIT, 9 live-coded classes (18 h) that take students from a first endpoint to Clean Architecture, JWT, Docker Compose and .NET Aspire. The material is versioned code with Testcontainers integration tests.

- ~16 cohorts and ~260 students so far: EducacionIT (~10 cohorts), Coderhouse backend courses in Node.js and C# (~5 cohorts of 30) and the national Argentina Programa 4.0 (50).



# Education
## **ISTEA**, Técnico Superior en Desarrollo de Software (3-year higher technical degree, completed 2026) -- Buenos Aires, AR
2023 – 2026



# Languages
**Spanish:** Native

**English:** Full professional proficiency (C1)
