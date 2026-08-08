# Book Agent Development Plan

## Project Vision

Build an AI reading companion that helps users understand books, discuss ideas, retain knowledge, and connect concepts across a lifetime of reading.

The goal is not only summarization, but a long-term intelligent reading partner.

## Architecture Roadmap

```
book-agent
├── agent            # Agent orchestration and runtime
├── skills           # Reusable agent capabilities
├── knowledge        # RAG and knowledge graph
├── memory           # User reading memory
├── tools            # External tools
├── api              # Service layer
└── docs             # Development documentation
```

## Development Phases

## Phase 1: Agent Runtime

Goal: establish the core agent execution framework.

Tasks:
- [ ] Agent base abstraction
- [ ] Agent lifecycle management
- [ ] Skill registration system
- [ ] Tool execution framework
- [ ] Session/context management

## Phase 2: Book Understanding Pipeline

Goal: enable book ingestion and understanding.

Tasks:
- [ ] Book file ingestion
- [ ] Document parsing
- [ ] Chapter extraction
- [ ] Summary generation
- [ ] Key concept extraction

## Phase 3: RAG Knowledge System

Goal: allow semantic book search and grounded answers.

Tasks:
- [ ] Vector storage
- [ ] Embedding pipeline
- [ ] Retrieval strategy
- [ ] Context assembly
- [ ] Answer generation

## Phase 4: Memory System

Goal: build persistent reading memory.

Tasks:
- [ ] Reading history
- [ ] User preferences
- [ ] Personal notes
- [ ] Long-term memory retrieval

## Phase 5: Knowledge Graph

Goal: connect concepts across books.

Tasks:
- [ ] Entity extraction
- [ ] Relationship modeling
- [ ] Concept graph
- [ ] Thought map generation

## Phase 6: Product Layer

Tasks:
- [ ] Web UI
- [ ] API service
- [ ] Authentication
- [ ] Deployment

## Development Rules

Every development session should:

1. Read DEVELOPMENT_PROGRESS.md first.
2. Complete a focused task.
3. Update progress after implementation.
4. Record important design decisions.
5. Commit changes with clear messages.
