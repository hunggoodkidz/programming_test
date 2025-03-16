import assignment_solved.Q1_sorting as q1_sorting
import assignment_solved.Q2_search as q2_search
import assignment_solved.Q3_hashtable as q3_hashtable
import assignment_solved.Q4_file_reader as q4_file_reader

def main():
    while True:
        print("\n")
        print("\n========= MENU =========")
        print("1. Questions 1 - Sorting")
        print("2. Questions 2 - Separate Chaining Index")
        print("3. Questions 3 - Edge-weighted digraph representation (HashTable)")
        print("4. Questions 4 - File Reader")
        print("5. Exit")
        print("========================")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            if hasattr(q1_sorting, "flight_sort_demo"):
                q1_sorting.flight_sort_demo()
            else:
                print("[ERROR] Q1_sorting.py is missing the function 'flight_sort_demo()'")

        elif choice == "2":
            if hasattr(q2_search, "search_demo"):
                q2_search.search_demo()
            else:
                print("[ERROR] Q2_search.py is missing the function 'search_demo()'")

        elif choice == "3":
            if hasattr(q3_hashtable, "hashtable_demo"):
                q3_hashtable.hashtable_demo()
            else:
                print("[ERROR] Q3_hashtable.py is missing the function 'main()'")

        elif choice == "4":
            if hasattr(q4_file_reader, "file_reader_demo"):
                q4_file_reader.file_reader_demo()
            else:
                print("[ERROR] Q4_file_reader.py is missing the function 'file_reader_demo()'")

        elif choice == "5":
            print("\n[INFO] Exiting the program. Goodbye!\n")
            break

        else:
            print("\n[ERROR] Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
