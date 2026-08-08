# Book Agent Architecture

## Overview

Book Agent uses a multi-agent architecture.

## Agents

### Orchestrator Agent
Responsible for task planning and routing.

### Reader Agent
Understands books and answers questions.

### Knowledge Agent
Builds semantic memory and knowledge graph.

### Learning Agent
Creates reviews, quizzes and learning summaries.

## Data Flow

```
Book -> Parser -> Embedding -> Knowledge Store -> Agent -> User
```

## Future Modules

- Vector database
- Graph database
- Long-term memory
- Skill marketplace
