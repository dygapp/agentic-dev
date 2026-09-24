# Current Architecture

## Current business year

Current state is inconsistent across planned/legacy Feature boundaries:

- one module reads a configuration table;
- one module reads user session state;
- one planned Feature proposes carrying a year in the request.

No stable system-wide responsibility or read contract has been accepted yet.

This file is the current Architecture owner for the decision.
