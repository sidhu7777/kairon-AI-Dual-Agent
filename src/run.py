
from graph.build_graph import graph_app

def main():
    query = input("Enter your research query: ")
    answer_type = input("Enter answer type (short/detailed): ").strip().lower()


    final_output = graph_app.invoke({
         "input_query": query,
        "answer_type": answer_type
    })

    print("\n=== Final Drafted Answer ===")
    print(final_output)

if __name__ == "__main__":
    main()

