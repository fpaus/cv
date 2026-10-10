# Fabrizio Dante Pauselli's CV

- Phone: +54 9 11 6975 9207
- Email: [fabriziopauselli@gmail.com](mailto:fabriziopauselli@gmail.com)
- Location: Buenos Aires, Argentina
- Website: [fpaus.github.iocv](https://fpaus.github.io/cv/)
- LinkedIn: [fabrizio-dante-pauselli-917365120](https://linkedin.com/in/fabrizio-dante-pauselli-917365120)
- GitHub: [fpaus](https://github.com/fpaus)


# Perfil
Arquitecto de software y Tech Lead con más de 10 años en ingeniería de software. Armé y dirigí el departamento de Arquitectura e Infraestructura Cloud de una fintech de remesas (6 ingenieros senior, más de 500 recursos de Azure bajo Terraform). Hoy lidero dos equipos (7 personas) sobre una plataforma .NET / Angular / Azure con .NET Aspire, y diseñé su forma de trabajo asistida por IA: agentes para revisión y QA, barrida de bugs autónoma, gateway LiteLLM, servidores MCP y skills de Claude Code, sostenidos por tests de arquitectura y desarrollo guiado por especificaciones.

# Habilidades
**Backend:** C#, .NET 8/10, ASP.NET Core Web API, Entity Framework Core, .NET Aspire, Hangfire, Native AOT, Avalonia, Node.js (NestJS), Python, Go

**Ingeniería de IA:** Gateway de LLMs y control de gasto (LiteLLM), Model Context Protocol (MCP), agentes de código (Claude Code, opencode, Antigravity), flujos multiagente y skills, contexto y memoria de agentes, revisión de código y QA asistidos por IA, LLMs locales (Ollama), reconocimiento de voz local (sherpa-onnx), guardrails de IA

**Cloud y DevOps:** Azure (App Service, Functions, SQL, Key Vault, Entra ID, identidades administradas, private endpoints, Application Insights), Terraform, GitHub Actions, Docker, OpenTelemetry

**Arquitectura y calidad:** Clean Architecture, SOLID, CQRS, ADRs, tests de arquitectura, ATDD, desarrollo guiado por especificaciones (OpenSpec), arquitectura como código (LikeC4), Testcontainers, Playwright, mutation testing (Stryker), PRs apilados, code review

**Frontend:** Angular, TypeScript, React, Next.js

**Datos:** SQL Server, PostgreSQL, SQLite, optimización de consultas

**Liderazgo:** Gestión de personas, evaluaciones de desempeño, onboarding, mentoría, planificación de iteraciones y capacidad, roadmaps técnicos, demos a stakeholders

# Experiencia
## **Arquitecto / Líder Técnico**, Craft-Labs -- Buenos Aires, AR

Mar 2026 – presente

- Lidero dos equipos de ingeniería (7 personas) que entregan en iteraciones de 2 semanas: planificación por capacidad, demos a stakeholders y roadmap técnico.

- Responsable de la arquitectura y la entrega de la plataforma de operaciones de la empresa (SOWs, asignaciones, facturación, feedback, compensaciones; ~20 pantallas, 8 roles) en .NET, Angular, Azure Functions y SQL Server con .NET Aspire.

- Diseñé el proceso de revisión asistido por IA que los equipos aplican a cada pull request: 5 agentes en paralelo (checks, estándares, spec, tests, seguridad) que cubren cadenas de hasta 13 PRs apilados y hacen valer los estándares que defino.

- Creé un proceso repetible de barrida de bugs autónoma con agentes en paralelo (12 rondas, ~9 agentes de fix por corrida). Primera corrida: 65 pull requests y 74 bugs rastreados hasta el cambio que los introdujo, en 7,5 horas sin intervención.

- Construí el proceso de QA de regresión asistido por IA (plan, ejecución, triage): los agentes derivan los casos de los PRs mergeados, los corren en Playwright con video y reportan los bugs. Primera pasada: 56 casos de 90 PRs, 10 bugs.

- Construí el sistema de calidad de la plataforma: tests de arquitectura, mutation testing (Stryker), ratchets de analizadores y lint, y suites de ~3.000 tests unitarios, 1.600 de integración (Testcontainers) y 4.400 de UI. Reduje el gasto de CI con checks bajo demanda y la integración local de 22 a 3 min.

- Reforcé la seguridad de la plataforma en Azure de punta a punta: acceso por identidad entre servicios, red cerrada y SQL Server restringido.

- Diseñé y construí el gateway de LLMs de toda la empresa (LiteLLM), para ingenieros y para productos con capacidades agénticas, con modelos locales y de suscripción, como despliegue productivo en Azure con gasto por equipo y modelo: Terraform (24 recursos), App Service, PostgreSQL privado, Key Vault, Entra ID, Application Insights, alertas de presupuesto.

- Construí el kit de desarrollo agéntico de los equipos: más de 30 skills de Claude Code para todo el ciclo (spec, cambio, revisión, QA, release, reportes) y una capa compartida de contexto y memoria entre agentes, para que todos trabajen igual con IA.

- Responsable del desarrollo de las personas: evaluaciones semanales a las 7, el plan de onboarding con el que incorporé 5 ingresos en 2026 y el ciclo de feedback de desempeño de toda la empresa como dueño del módulo.



## **Lead Architect**, Remitee -- Buenos Aires, AR

Feb 2023 – Feb 2026

- Armé y dirigí el departamento de Arquitectura e Infraestructura Cloud de una fintech de remesas internacionales: contraté a sus 6 arquitectos e ingenieros cloud senior (dos equipos), llevé sus evaluaciones de desempeño y desarrollo de carrera, y ayudé a contratar para otros equipos.

- Lideré el proyecto que puso más de 500 recursos de Azure bajo Terraform y bajó el aprovisionamiento de horas o días de trabajo manual a menos de una hora.

- Lideré la separación de un monorepo de ~50 microservicios en un repositorio por servicio y su migración de .NET Core 2 a .NET 6 y 8.



## **Líder Técnico**, SoulIT -- Buenos Aires, AR

Feb 2022 – Feb 2023

- Lideré dos equipos de desarrollo en simultáneo (3 a 4 ingenieros cada uno) con prácticas ágiles.



## **Arquitecto de Software (part-time)**, Consultoría independiente -- Remoto

Ene 2019 – presente

- Diseñé la arquitectura de un hub de cobranzas para un banco mayorista (2026), de los requerimientos al diseño aprobado: modelo LikeC4 de 21 vistas, 7 ADRs y 19 decisiones sobre Spring, Kafka con outbox/inbox, Keycloak y OpenShift, para 5.000 TPS.



## **Desarrollador · Analista QA**, Sector público: ANSES, Ministerios de Producción y Trabajo -- Buenos Aires, AR

May 2015 – Sep 2019

- Desarrollo en equipos Ágiles (2018–2019) tras tres años de testing manual y automatizado (2015–2018).



# Proyectos destacados
**Unified Workbench:** Producto construido con agentes: app de escritorio .NET / Avalonia más hosts MCP (~37 tools) para reportes diarios, tableros de GitHub y análisis de esfuerzo. Lo diseñé (24 ADRs, modelo LikeC4, tests de arquitectura) y su backlog de ~380 issues lo implementaron subagentes de Claude Code en paralelo, con costo en tokens por ticket; más de 960 tests.

**Open source:** pnpm/pnpm#15724 (mergeado): fix de los shims `.cmd` de Windows rotos por un `%` en la ruta, en Rust y TypeScript con tests. microsoft/aspire#20652: falla de `WithRepl` de SQL con scripts CRLF.

# Docencia y mentoría
## **Docente**, Coderhouse & EducacionIT -- Buenos Aires, AR

Ene 2023 – presente

- Creé y dicto el curso "Web APIs con .NET" en EducacionIT: 9 clases en vivo (18 h) de un primer endpoint a Clean Architecture, JWT, Docker Compose y .NET Aspire, con material versionado y tests de integración (Testcontainers).

- Unas 16 cohortes y ~260 alumnos: EducacionIT (~10 cohortes), cursos de backend Node.js y C# en Coderhouse (~5 cohortes de 30) y el programa nacional Argentina Programa 4.0 (50).



# Educación
## **ISTEA**, Técnico Superior en Desarrollo de Software (3 años, título emitido en 2026) -- Buenos Aires, AR
2023 – 2026



# Idiomas
**Español:** Nativo

**Inglés:** Avanzado, uso profesional (C1)
