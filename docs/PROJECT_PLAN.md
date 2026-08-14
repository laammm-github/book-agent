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

Status: Mostly completed foundation

Completed:
- [x] Agent base abstraction
- [x] Agent lifecycle management
- [x] Skill registration system foundation
- [x] Tool abstraction foundation
- [x] Tool registry foundation
- [x] Session/context foundation
- [x] Runtime execution executor foundation

Remaining:
- [ ] Complete production-grade skill execution workflow
- [ ] Complete tool execution framework

## Phase 2: Book Understanding Pipeline

Status: In Progress

Goal: enable book ingestion and understanding.

Completed:
- [x] Book file ingestion abstraction
- [x] Document parsing foundation
- [x] Chapter extraction foundation
- [x] Metadata parsing foundation
- [x] TXT loader
- [x] PDF loader foundation
- [x] EPUB loader foundation

Remaining:
- [ ] Complete PDF extraction
- [ ] Complete EPUB extraction
- [ ] Add parser integration pipeline
- [ ] Generate knowledge objects
- [ ] Add summary generation
- [ ] Add key concept extraction

## Phase 3: RAG Knowledge System

Status: Planned

Tasks:
- [ ] Vector storage
- [ ] Embedding pipeline
- [ ] Retrieval strategy
- [ ] Context assembly
- [ ] Answer generation

## Phase 4: Memory System

Status: Planned

Tasks:
- [ ] Reading history
- [ ] User preferences
- [ ] Personal notes
- [ ] Long-term memory retrieval

## Phase 5: Knowledge Graph

Status: Planned

Tasks:
- [ ] Entity extraction
- [ ] Relationship modeling
- [ ] Concept graph
- [ ] Thought map generation

## Phase 6: Product Layer

Status: Planned

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
