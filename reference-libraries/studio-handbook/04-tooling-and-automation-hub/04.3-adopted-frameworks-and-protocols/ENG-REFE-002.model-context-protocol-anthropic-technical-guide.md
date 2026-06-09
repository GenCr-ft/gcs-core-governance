---
docId: ENG-REFE-002
title: Model Context Protocol (MCP) — Technical Guide
version: 1.0.0
authors:
- AI Compliance Agent
creation_date: '2025-05-26'
language: en
last_updated_date: '2026-05-20'
metadata:
  lifecycle-stage: approved
  keywords:
  - technical-writing
  - model-context-protocol
  - anthropic
  - ai-tools
  - architecture
  - interoperability
  scope: studio
  domain: engineering
  doc-type: reference
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/04-tooling-and-automation-hub/04.3-adopted-frameworks-and-protocols/ENG-REFE-002.model-context-protocol-anthropic-technical-guide.md
---
# Anthropic's Model Context Protocol (MCP): Technical Guide for Software Architects and AI Agents

## 0. Context and Adoption by Gencraft Studio

**Gencraft Studio Note:** This document is an integration into our SSoT of a reference technical guide on the **Model Context Protocol (MCP)**, largely inspired by Anthropic's work and community analysis. Gencraft Studio has made the strategic decision to adopt the **Model Context Protocol (MCP)** as a fundamental standard to normalize how its AI Gems interact with the `Tools` that provide them with extended capabilities.

The use of MCP aims to:

- Ensure maximum **interoperability** between Gems and a wide range of `Tools` (internal or external).
- Promote **modularity** and **reusability** of `Tools` by exposing them via compliant **MCP Servers**.
- Simplify development and integration of new capabilities for our Gems.
- Provide a secure and standardized framework for Gem-Tool interactions.

This document serves as the **primary technical reference** for all architects (`Isaac`), developers (Gems and humans), and AIE Team members involved in the design, development, or use of Gems, `Tools`, and MCP Servers within Gencraft. Gencraft-specific implementations, our own Core Studio Services acting as MCP Servers, and our Gems' `Tools` are detailed in other SSoT documents (notably in `04-tooling-and-automation-hub/`, Core Studio Services TDDs, and Gem Blueprints).

---

## 1. Introduction to the Model Context Protocol (MCP)

The AI application development landscape is evolving rapidly, with increasing demand for AI agents capable of interacting more dynamically and contextually with their environment. At the heart of this evolution is the need to standardize how large language models (LLMs) access and use external data and tools. In this context, Anthropic introduced the Model Context Protocol (MCP).

### 1.1. Definition and Fundamental Objectives of MCP

The Model Context Protocol (MCP) is an open standard developed by Anthropic, designed to normalize how AI applications—whether conversational agents, development assistants, or custom agents—connect and interact with external tools, data sources, and systems. [1] Often described using the analogy of a "USB-C port for AI applications" [1], MCP aims to provide a universal and standardized interface, similar to how USB-C unified connectivity for peripherals. Before standards like USB, connecting peripherals required a multitude of different ports and custom drivers. Similarly, integrating AI applications with M applications and N external tools/systems represented an M×N complexity problem, potentially requiring M×N distinct integrations. [2] MCP aims to transform this challenge into an M+N complexity problem, where tool creators build N MCP servers (one for each system) and application developers build M MCP clients (one for each AI application). [2]

The fundamental objectives of MCP are multiple and aim to solve several challenges inherent in LLM integration:

- **Universal and standardized access**: Establish a unique and open protocol that AI assistants (MCP clients) can use to query or retrieve data and context from various sources. [5]
- **Secure and normalized connections**: Replace the need for ad hoc API connectors or custom wrappers with a protocol that handles authentication, usage policies, and standardized data formats. [6]
- **Durability and ecosystem**: Cultivate an ecosystem of reusable connectors ("MCP servers") that developers can build once and reuse across multiple LLMs and clients, eliminating the need to rewrite the same integration in many different ways. [6]
- **Simplified integration**: Reduce complexity and redundancy in building AI-powered workflows by standardizing how agents discover, access, and interact with external data and tools. [5]

### 1.2. Importance and Key Use Cases for Software Architects

For software architects, understanding and potentially adopting MCP is of strategic importance. The protocol offers concrete solutions to recurring architectural problems in AI system development. Its importance stems from several factors:

- **More relevant AI**: LLMs, even advanced ones, are often trained on incomplete or outdated datasets. By connecting them to live data—whether Google Drive documents, official API documentation, Slack messages, or an internal database—MCP helps ensure that model responses are up-to-date, context-rich, and domain-specific. [6]
- **Unified data access**: Before MCP, a developer might have had to juggle separate plugins, tokens, or custom wrappers to give an AI system access to multiple sources. With MCP, a single protocol is configured, allowing the LLM to "see" all registered connectors, promoting a more uniform and standardized ecosystem. [6]
- **Long-term maintainability**: Ad hoc solutions become a nightmare as the organization adds data sources. MCP's open and standardized approach means fewer breakages and simpler debugging. Instead of rewriting integrations with every new platform adoption, one can rely on a shared library of MCP servers. [6]

The benefits for companies adopting MCP are significant and include the ability to build more effective AI agents, simplify integration, reduce development costs, improve security and control, and future-proof their AI strategy. [8]

MCP use cases are varied and touch many areas where AI agents can add substantial value:

- IT support bots [5]
- Development assistants [5]
- Intelligent document processing [8]
- Knowledge synthesis for research [8]
- Architecture, Engineering, and Construction (AEC) project coordination [8]
- AI assistants managing calendars or other business systems [9]
- Secure AI in the healthcare sector [9]

Adopting MCP allows architects to design systems where AI agents are no longer isolated silos but active participants capable of drawing from the organization's collective knowledge and acting on its behalf, leading to more accurate, contextual, and valuable results. [8]

## 2. Understanding MCP Architecture and Key Concepts

To effectively use MCP, a software architect must master its underlying architecture and the fundamental concepts governing interactions between different components. MCP draws inspiration from proven standardization successes such as web APIs and the Language Server Protocol (LSP), explicitly extending this lineage of standardization to the AI domain. [11]

### 2.1. MCP Client-Server Architecture

MCP adopts a client-server architecture, or more precisely a client-host-server model, to structure communications and context sharing. [2] This architecture is designed to be modular, scalable, and adaptable to various LLM applications and environments. [12]

The main components of this architecture are:

- **Hosts**: These are the applications with which the user interacts directly, such as Claude Desktop, Integrated Development Environments (IDEs) like Cursor, or custom AI agents. [2] The host is the environment where the LLM resides and which initiates communication. It acts as a container or coordinator for multiple client instances, managing their lifecycle and security policies (permissions, user authorization, consent). [9]
- **Clients**: Integrated within hosts, MCP clients are lightweight protocol clients that handle communication with a specific MCP server. [2] Each client maintains a one-to-one (1:1) and stateful connection with an MCP server. [3] The client is responsible for negotiating capabilities and orchestrating messages between itself and the server, while maintaining security boundaries. [9]
- **Servers**: These are independent programs or processes that expose specific capabilities (data, tools, prompts) via the MCP standard. [2] MCP servers act as bridges or APIs between the MCP world and the specific functionality of an external system (a third-party API, a database, local files, etc.). [2] They encapsulate these external capabilities and present them in accordance with the MCP specification.

Before any meaningful communication can begin, an initialization phase, or *handshake*, is crucial. [2] This process proceeds as follows:

1. The client sends an `initialize` request to the server. This request includes the protocol version supported by the client and its capabilities. [2]
2. The server responds with its own protocol version and a list of the capabilities it offers. [2]
3. Finally, the client sends an `initialized` notification to the server to acknowledge receipt and confirm that the handshake is complete. [2] This handshake ensures basic interoperability. [14]

### 2.2. Fundamental Components: Tools, Resources, and Prompts

MCP defines three main types of "capabilities" that servers can expose: [2]

- **Tools**:
  - **Definition**: Functions or actions that the LLM can invoke to perform operations, interact with external systems, or carry out calculations. They are "model-controlled". [2]
  - **Structure**: JSON including `name`, `description`, `inputSchema` (JSON Schema), and optional `annotations` (like `readOnlyHint`, `destructiveHint`, `idempotentHint`). [11, 17]
  - **Examples**: Querying a database, sending an email, creating a support ticket. [5]
- **Resources**:
  - **Definition**: Data or content that the LLM can read to gain context. They are "application-controlled" and read-only. [2]
  - **Structure and Access** [18]: Identified by URIs. Can be textual (UTF-8) or binary (base64). Clients read via `resources/read`. Servers notify changes via `notifications/resources/list_changed` or `notifications/resources/updated` (for subscribed resources).
  - **Examples**: File content, database records, system logs. [2]
- **Prompts (User-controlled)**:
  - **Definition**: Predefined templates or workflows exposed by servers that users explicitly select to initiate specific interactions. [2] They are "user-controlled".
  - **Structure and Use** [20]: Servers list prompts via `prompts/list`. A client requests a prompt via `prompts/get`, and the server returns a message structure defining the interaction flow.
  - **Examples**: "Generate a Git commit message", "analyze project logs". [19]

This clear distinction between actions (Tools), passive context (Resources), and guided interactions (Prompts) is fundamental.

### 2.3. Communication Protocols (Transports)

MCP uses JSON-RPC 2.0 as the message format and is transport-agnostic. [7, 14]

- **stdio (Standard Input/Output)**:
  - **Operation**: Communication via a process's standard input/output streams. [2]
  - **Use case**: Ideal for local integrations (same machine). [2]
- **HTTP with SSE (Server-Sent Events)**:
  - **Operation**: Unidirectional server-to-client streaming via HTTP. Client-to-server POST requests. [2, 13]
  - **Use case**: Networked services, real-time updates from server to client. [2]
- **Streamable HTTP (Future Evolution)**:
  - Aims for more flexible and robust bidirectional communication over HTTP, better state management, and scalability. [19]

The choice of transport depends on the application's needs.

## 3. Why Use MCP? Benefits and Value Add

### 3.1. Increased Standardization and Interoperability

- **A universal standard**: Like REST for web services or LSP for IDEs. [2, 24]
- **M×N complexity reduction**: Simplifies architecture by moving to M+N integrations. [2]
- **Interoperability and flexibility**: Open protocol, model-agnostic, promoting "plug-and-play". [3, 14, 24]

### 3.2. Extended Capabilities for AI Agents

- **"Eyes and hands" for AI**: Allows agents to actively interact with the digital world. [5]
- **Real-time data access and concrete actions**: Goes beyond frozen knowledge, allows interaction with business systems (Slack, Salesforce, Jira, GitHub). [5]
- **Autonomous execution of complex tasks**: Foundation for agents capable of planning, using tools, reasoning over organizational data, and adapting. [8]

### 3.3. Simplified Development and Maintenance

- **Reduced costs and delays**: Fewer integration challenges, focus on agent logic. [5]
- **Improved long-term maintainability**: Changes isolated in MCP servers, protecting the client application. [4]
- **Modular architecture**: Adding/removing capabilities with minimal disruption. [5]

### 3.4. Enhanced Security and Control

- **Integrated security**: Permission control and security boundaries are integral aspects. [5, 8]
- **Explicit control mechanisms**: User consent, clear permissions, granular access. [8]
- **Standardized authentication**: Relies on OAuth 2.0 / 2.1 for secure communications. [21]

## 4. AI Agent Interaction Mechanisms with MCP

### 4.1. Dynamic Capability Discovery (Tools, Resources, Prompts)

- **Capability querying**: The client requests `tools/list`, `resources/list`, `prompts/list`. [2]
- **Server response**: Provides lists with metadata (name, description, inputSchema for tools). [2, 18, 20]
- **Change notifications**: Servers can notify clients of changes (`notifications/tools/list_changed`, etc.). [17]

### 4.2. Tool Selection and Invocation by the AI Agent

- **LLM decision-making**: The LLM chooses the tool based on the user request, context, and tool descriptions/schemas. [5, 16]
- **Tool invocation**: The client sends a `tools/call` request with the tool name and parameters (conforming to the inputSchema). [10]
- **Execution and results return**: The MCP server executes the tool and returns the result or an error to the client. [2]
  - Metadata quality (descriptions, schemas) is crucial for effective tool selection by the LLM. [16, 30]

### 4.3. Context and Conversation Management

- **Integration of tool results**: Tool results are fed back into the LLM's context for more relevant responses. [2]
- **Role of parameterized prompts and descriptions**: MCP prompts guide interactions. Natural language descriptions of tools help the LLM reason about their use and chain them together. [16, 31]
- **Multi-turn context management and handoffs**: MCP facilitates context consistency. Tools like `mcp-cli` [33] help manage history. MCP can support complementary A2A (agent-to-agent) protocols. [34]
- **LLM context window optimization**: Tools can return filtered information or summaries to minimize contextual load. [31, 36]

### 4.4. Error Handling and Recovery Strategies

- **Error return by the MCP server**: In case of failure, the server returns a structured error response. [17]
- **Error analysis by the agent**: The agent analyzes the error to understand the cause. [39]
- **Recovery attempts [13]**:
  - Parameter correction.
  - Use of an alternative tool.
  - Retry with backoff.
  - Asking the user for clarification.
  - Alternative planning.
- Importance of state management for complex flows. [25]

### 4.5. Orchestration of Multiple and Dependent MCP Tool Calls

- **Agent orchestration layer**: Maintains state, memory, reasoning strategies (ReAct, Chain-of-Thought). [35]
- **Multi-step planning and execution**: The agent breaks down tasks, calls tools sequentially, with results informing subsequent steps. [8]
- **Amazon Bedrock Agents example [42]**: Orchestration of calls to distinct MCP clients (Cost Explorer, Perplexity AI) and Code Interpreter for a composite response.
- **Results synthesis**: The orchestration layer tracks and synthesizes information before the final response. [35]

## 5. Practical Implementation: Building with MCP

### 5.1. Available SDKs and Libraries

- **Official SDKs**: Anthropic provides SDKs for Python, TypeScript, and plans for Java, Kotlin, C#. [2]
  - Python (`mcp` package): Includes FastMCP, `ClientSession`, transports (`stdio_client`, `streamablehttp_client`). [2, 6, 15]
  - TypeScript (`@modelcontextprotocol/ts-sdk`). [23]
- **Community Libraries**: FastMCP (Python) [44], `cyanheads/model-context-protocol-resources` [23].

**Table 1: MCP SDKs and Libraries (excerpt from original document)**

| Language   | SDK/Library Name                       | Main Features                                                            | Status            | Link (Example)                                      |
| :--------- | :------------------------------------- | :----------------------------------------------------------------------- | :---------------- | :-------------------------------------------------- |
| Python     | `mcp` (including FastMCP)               | Client/server support, transports, easy tool/resource definition        | Official          | GitHub - modelcontextprotocol/python-sdk [19]       |
| TypeScript | `@modelcontextprotocol/ts-sdk`         | Client/server support, transports, strong typing                         | Official          | (Doc MCP general) [3]                               |
| Python     | `jlowin/fastmcp`                       | High-level abstraction, OpenAPI/FastAPI support                          | Community/Core   | GitHub - jlowin/fastmcp [44]                        |
| ...        | ...                                    | ...                                                                      | ...               | ...                                                 |

### 5.2. Building an MCP Server (Python Examples with FastMCP)

- **Initialization**: `mcp_server = FastMCP("ServerName")` [6]
- **Tool Definition**: Using `@mcp_server.tool()` decorators. Docstrings and type annotations generate MCP schemas. [6, 44]

    ```python
    # Example with FastMCP [44]
    # from fastmcp import FastMCP
    # mcp_server = FastMCP("WeatherServer")
    # @mcp_server.tool()
    # async def get_forecast(latitude: float, longitude: float) -> str:
    #     """Retrieves weather forecast for a given location."""
    #     return f"Forecast for {latitude},{longitude}: Sunny, 25°C" # Placeholder
    ```

- **Resource Definition**: `@mcp_server.resource("uri_template")` decorator. [19, 44]

- **Prompt Definition**: `@mcp_server.prompt()` decorator. [19, 44]
- **Server Execution**: `mcp_server.run(transport='stdio')` [6]

### 5.3. Developing an MCP Client (AI Agent - Python Examples)

- **Connection and Session**: Use `ClientSession` and transports (`stdio_client`, `streamablehttp_client`). `StdioServerParameters` for local servers. [2]

    ```python
    # Conceptual example of stdio client connection
    # from mcp import ClientSession, StdioServerParameters
    # from mcp.client.stdio import stdio_client
    # server_params = StdioServerParameters(command="python", args=["path/to/your_mcp_server_script.py"])
    # async with stdio_client(server_params) as (read_stream, write_stream):
    #     async with ClientSession(read_stream, write_stream) as session:
    #         await session.initialize()
    #         # ... interact with the server ...
    ```

- **Capability Discovery and Invocation**:
  - List tools: `tools_response = await session.list_tools()` [2]
  - Call tool: `result = await session.call_tool("tool_name", arguments={"param": "value"})` [2]
  - Read resource: `content, mime_type = await session.read_resource("uri")` [19]
  - Get prompt: `prompt_data = await session.get_prompt("prompt_name", arguments={...})` [19]

### 5.4. Enhancing AI Agents with RAG via MCP

- **RAG and MCP**: The retrieval component of a RAG system can be exposed as an MCP server, allowing standardized access to external context for the LLM. [51]
- **Examination of the `mcp-local-rag` server [52]**:
  - **Functionality**: Web search (DuckDuckGo), embedding retrieval (Google MediaPipe), similarity calculation, HTML content extraction, conversion to Markdown for the LLM.
  - **Flow**: AI Agent sends query -> `mcp-local-rag` executes search/processing pipeline -> returns Markdown context -> AI Agent uses context to generate response.
  - This demonstrates that MCP standardizes access to information retrieval tools, crucial for RAG, paving the way for increased modularity of RAG systems.

## 6. Strategic Considerations for Software Architects

### 6.1. MCP Security: Authentication (OAuth), Authorization, and Secure Design

- **Authentication**: MCP relies on **OAuth 2.0 / 2.1** (with mandatory PKCE). [21, 27]
  - MCP Server = OAuth 2.1 resource server.
  - MCP Client = OAuth 2.1 client.
  - Authorization Server (integrated or external) issues access tokens.
  - MCP servers should expose standard metadata (RFC 8414) for authorization endpoint discovery. [27]
- **Authorization and Permissions**: Clear permission models, granular access controls, explicit user consent. [8] The "Roots" concept helps define operation scopes for servers. [11]
- **Secure Data Management and Best Practices [17]**:
  - Validate all inputs, sanitize paths/commands, validate external URLs/IDs, check parameter sizes/ranges.
  - Deploy focused MCP servers with limited permissions.
  - Audit tool usage, use HTTPS for remote communications.
  - Do not expose internal errors, log security errors.
- **Identified Security Challenges [25]**: Server name collisions, installer spoofing, code injection, tool name conflicts, sandbox escapes, privilege persistence, etc. Necessity of secure installation frameworks and strict naming policies.

### 6.2. Comparison: MCP vs. Custom Integrations, ChatGPT Plugins, and Others

**Table 2: MCP vs. Alternative Integration Approaches (excerpt from original document) [4]**

| Aspect                  | Model Context Protocol (MCP)                                  | Custom API Integrations                        | Proprietary Plugin Systems (e.g., ChatGPT)      | Agent Frameworks (e.g., LangChain)                 |
| :---------------------- | :------------------------------------------------------------ | :--------------------------------------------- | :---------------------------------------------- | :------------------------------------------------- |
| Integration Speed       | Fast (if MCP server exists) [21]                              | Slow (custom code) [21]                        | Medium (proprietary plugin) [21]               | Medium (custom code for tools) [21]                |
| Standardization         | High (open protocol) [1]                                      | Low (ad hoc) [24]                              | Medium (platform standard) [21]                | Medium (framework standard) [29]                   |
- **Structured**: Pydantic models (BaseModel).
| Modularity              | High (distinct MCP servers) [5]                               | Low (often monolithic)                         | Limited by platform                             | Good (agent code), depends on tool integrations    |
| Maintainability         | Good (isolated server changes) [4]                            | Difficult (external API impact)                | Depends on maintainer/platform                  | Depends on tool integrations and framework stability |
| Interaction Richness    | Continuous, context-rich (Tools, Resources, Prompts) [21]      | Ad hoc, single request/response [21]           | Mainly "single-shot" [21]                      | Context managed by agent logic, complex [21]       |
| Ecosystem               | Rapidly growing, open [9]                                     | N/A (specific)                                 | Closed, platform-specific                       | Large (LangChain Hub), variable quality            |
| Control/Flexibility     | Good (control over MCP servers)                               | Maximal (total control)                        | Limited by platform                             | Good (agent logic), tools = black boxes           |

MCP offers a trade-off: increased standardization and maintainability vs. total control of custom integrations. More open than proprietary plugins. Complementary to agent frameworks by standardizing the agent-tool interface.

### 6.3. Architecturing for Success: Scalability, Maintainability, and Modularity

- **Modularity**: AI systems built from small, specialized, reusable MCP servers. [5] Similar to SOA/microservices for AI capabilities. [32]
- **Maintainability**: Changes contained within the corresponding MCP server, isolating the client. [4]
- **Scalability**: MCP servers can be deployed and scaled independently. [25] Challenges may arise in multi-tenant environments. [25]

### 6.4. Best Practices for Design and Implementation of MCP-Compatible AI Agents

- **MCP Tool Design**: Focus on specific user goals rather than wrapping full APIs. [40, 53]
- **Tool Descriptions for the LLM**: Critical clarity and completeness. Include examples, edge cases, input format, distinctions. [40]
- **Evaluation Tests ('evals')**: Measure the agent's ability to use tools correctly. [40, 53]
- **Scoped Permissions**: Deploy multiple small, focused MCP servers with limited permissions. [53]
- **Agent Simplicity and Transparency**: Aim for simplicity, make agent planning transparent. [40]
- **"Poka-Yoke" (Error-Proofing) Design**: Modify argument/tool design to reduce LLM errors. [40]
- **MCP Interaction Isolation**: Isolate MCP interaction logic from the rest of the application. [32]
- **MCP is not a Panacea**: Does not solve fundamental problems of poor info retrieval, inefficient memory selection, or injudicious tool use by the LLM. [32]
- **LLM Context Window Management**: Tools can return summaries/filtered data to not overload context. [31]
- Efficiency depends on the **quality of the interface** exposed by MCP servers (descriptions, parameters) for the LLM. [16, 40] This is akin to prompt engineering applied to tool design.
- MCP encourages **contract-driven design** for AI agent capabilities. [1, 12, 17] The emergence of MCP server marketplaces (Smithery, Glama [34]) indicates this trend.

## 7. The Evolving Landscape of MCP

### 7.1. Adoption, Community, and Growing Ecosystem

- **Industry Adoption**: Google, Microsoft, OpenAI, Replit, Zapier, Snowflake, Cloudflare, etc. [5]
- **Connector and Server Growth**: Over 1000 open-source connectors as of Feb 2025. [9] The official `modelcontextprotocol/servers` repository [47] hosts dozens of reference implementations.
- **Community Resources**: GitHub repositories (e.g., `cyanheads/model-context-protocol-resources` [23]), documentation, SDKs, tools (MCP Inspector [2]).
- **Emerging Marketplaces**: Smithery, Glama. [34]

### 7.2. Future Trajectory: Potential Developments and Emerging Challenges

- **Challenges to Address**:
  - Security for remote/cloud deployments. [24]
  - Large-scale tool discovery. [24]
  - Version management and server drift. [25]
  - Complex state management and error recovery. [25]
  - Inter-server authentication/authorization (MCP nesting [31]).
  - Comprehensive debugging and monitoring. [25]
- **Potential Developments**:
  - Integration with inter-agent (A2A) protocols. [5]
  - MCP as a lightweight coordination layer within a broader infrastructure (identity, policies, data governance, observability). [56]
- Long-term success will depend on the ability to address security and governance challenges in a distributed ecosystem. [3, 25, 32] A robust trust and management framework is necessary.

## 8. Conclusion and Strategic Recommendations

MCP is a breakthrough for standardization, modularity, and extended AI agent capabilities, paving the way for an interoperable "agentic enterprise". [8]

**Recommendations for Architects:**

1. Start with well-defined use cases.
2. Invest in high-quality MCP server design (clear descriptions for LLMs, contract-driven design).
3. Implement robust security strategies from the start (OAuth 2.1, granular permissions).
4. Prioritize a modular and composable approach.
5. Actively track standard and ecosystem evolution.
6. Integrate with solid software engineering practices (testing, versioning, documentation).

MCP is a powerful tool but must be combined with solid agent design and an understanding of its implications.

## Citation Sources (Examples)

1. Model Context Protocol (MCP) - Anthropic, accessed May 17, 2025, `https://docs.anthropic.com/en/docs/agents-and-tools/mcp`
2. Model Context Protocol (MCP) an overview - Philschmid, accessed May 17, 2025, `https://www.philschmid.de/mcp-introduction`
3. Model Context Protocol: Introduction, accessed May 17, 2025, `https://modelcontextprotocol.io/introduction`
    ... (and so on for all sources)

---
*This document is a technical reference resource. Gencraft-specific implementations and standards for MCP use are described in the relevant SSoT documents (e.g., ADRs, Core Studio Services TDDs, `ai-tool-development-standards.md`).*

## AI Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
