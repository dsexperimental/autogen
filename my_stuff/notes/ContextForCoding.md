# Context Generation for a Coding  Assistant

One of the biggest challenges for a coding assistant is loading the needed context for the assistant to do a task.

I want to think about a command line method for doing this. (Later we can create a UI.) We will have commands for the user to create the
context, adding files and "objects" (function, class, type...) either whole or as "documentation" to it.

## Language server idea:

Here is a summary of a workflow using a language server to get documentation on individual objects from a code base.

(NOTE _ WE CAN ALSO USE THE WORKSPACE SYMBOL REQUEST TO LOOK UP A WHOLE "FUNCTION")

### Goal
To generate detailed context information for a codebase, allowing users to specify functions, classes, and other objects via a CLI command. This context information will be used to assist in various coding-related tasks and improve developer interaction with the code.

### Workflow Steps

1. **User Input**:
   - Users provide the names of functions, classes, or other objects they want to add to the context by typing them into the CLI with a specific command.

2. **Workspace Symbol Request**:
   - Upon receiving user input, your tool makes a "workspace symbol" request to the Language Server. This request searches the entire workspace (all files in the project) for the specified symbol (e.g., function or class name).
   - The Language Server responds with a list of symbols that match the query, including their locations (file paths and positions within the file).

3. **Hover Request**:
   - For each symbol identified in the workspace symbol search, your tool then sends a "hover" request to the Language Server, targeting the specific location (file and position) of the symbol.
   - The hover request is designed to fetch detailed information about the code at the specified position. This typically includes the symbol's signature (like the function signature with parameter types) and any associated documentation (e.g., docstrings, JSDoc comments).

4. **Compilation of Context Information**:
   - The responses from the hover requests are processed and compiled into a structured context format. This context includes detailed information about each function, class, or object that the user specified, enriched with type signatures and descriptions.

5. **Presentation to the User**:
   - The compiled context information is then presented back to the user via the CLI, allowing them to understand and interact with the codebase more effectively.

### Considerations

- **Performance**: The process involves several requests to the Language Server, especially for large codebases with multiple matches. Efficiency should be considered.
- **Accuracy and Relevance**: Ensure that the tool correctly interprets user input and retrieves the most relevant information.
- **Future UI Integration**: While the initial implementation is CLI-based, consider how this workflow might integrate with a future UI for even smoother user interaction.

This workflow leverages the capabilities of a Language Server to provide an efficient and accurate method for users to gather contextual information about their codebase through a simple CLI interface.