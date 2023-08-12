#include <stdio.h>
#include <stdlib.h>
#include <igraph/igraph.h>

int main() {
    FILE *input_file = fopen("input.txt", "r");
    if (input_file == NULL) {
        perror("Error opening input file");
        return 1;
    }

    int rows, cols;
    fscanf(input_file, "%d %d", &rows, &cols);

    // Read and ignore the initial state
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            int value;
            fscanf(input_file, "%d", &value);
        }
    }

    int num_actions;
    fscanf(input_file, "%d", &num_actions);

    // Read the actions and build the graph
    igraph_t graph;
    igraph_vector_t edges;
    igraph_vector_init(&edges, 0);

    for (int i = 0; i < num_actions; i++) {
        int num_indices;
        fscanf(input_file, "%d", &num_indices);

        int action[num_indices];
        for (int j = 0; j < num_indices; j++) {
            fscanf(input_file, "%d", &action[j]);
        }

        for (int k = 0; k < rows * cols; k++) {
            igraph_vector_push_back(&edges, k);
            for (int j = 0; j < num_indices; j++) {
                igraph_vector_push_back(&edges, (k + action[j]) % (rows * cols));
            }
        }
    }
    
    igraph_create(&graph, &edges, 0, 0);
    igraph_vector_destroy(&edges);

    // Perform DFS to find a cycle
    igraph_stack_t stack;
    igraph_bool_t found_cycle = 0;
    igraph_stack_init(&stack, 0);
    igraph_dfs(&graph, 0, IGRAPH_OUT, 1, 0, 0, 0, &stack, 0, 0, 0, &found_cycle);

    // Print the cycle if found
    if (found_cycle) {
        printf("Cycle found:\n");
        igraph_stack_t copy_stack;
        igraph_stack_clone(&copy_stack, &stack);
        while (!igraph_stack_empty(&copy_stack)) {
            igraph_integer_t vertex = igraph_stack_pop(&copy_stack);
            printf("%d ", vertex);
        }
        printf("\n");
    } else {
        printf("No cycle found.\n");
    }

    // Free resources
    igraph_stack_destroy(&stack);
    igraph_destroy(&graph);
    fclose(input_file);

    return 0;
}

