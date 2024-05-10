class Librerias:
    def __init__(self):
        # Inicialización de la lista de tareas
        self.task = []

    def add_task(self, task):
        # Método para agregar una nueva tarea a la lista
        self.tasks.append(task)

    def complete_task(self, task_index):
        # Método para marcar una tarea como completada
        if 0 <= task_index < len(self.tasks):  # Verifica si el índice de tarea es válido
            self.tasks[task_index]['completed'] = True  # Marca la tarea como completada
        else:
            raise IndexError("Invalid task index")  # Si el índice no es válido, genera una excepción

    def delete_task(self, task_index):
        # Método para eliminar una tarea de la lista
        if 0 <= task_index < len(self.tasks):  # Verifica si el índice de tarea es válido
            del self.tasks[task_index]  # Elimina la tarea de la lista
        else:
            raise IndexError("Invalid task index")  # Si el índice no es válido, genera una excepción

    def show_tasks(self):
        # Método para mostrar todas las tareas en la lista
        if not self.tasks:  # Verifica si la lista de tareas está vacía
            print("No tasks.")  # Si está vacía, muestra un mensaje indicando que no hay tareas
        else:
            for i, task in enumerate(self.tasks):  # Recorre la lista de tareas
                status = "completed" if task['completed'] else "pending"  # Determina el estado de la tarea
                print(f"{i+1}. {task['description']} - {status}")  # Muestra la descripción y estado de la tarea

def main():
    task_manager = Librerias()  # Instancia un objeto de la clase TaskManager
    while True:
        print("\nLibros anonimos")
        print("1. Add Libros")
        print("2. Complete Libros")
        print("3. Show Libros")
        print("4. Delete Libros")
        print("5. Exit")

        try:
            choice = int(input("Introduce el numero de la opcion: "))  # Solicita al usuario que ingrese una opción
            if choice == 1:
                description = input("Enter task description: ")
                task_manager.add_task({'description': description, 'completed': False})
            elif choice == 2:
                task_index = int(input("Enter task index to mark as completed: ")) - 1
                task_manager.complete_task(task_index)
            elif choice == 3:
                task_manager.show_tasks()
            elif choice == 4:
                task_index = int(input("Enter task index to delete: ")) - 1
                task_manager.delete_task(task_index)
            elif choice == 5:
                break  # Si el usuario elige salir, termina el bucle
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except IndexError as e:
            print(e)  # Maneja la excepción de índice no válido

if __name__ == "__main__":
    main()  # Llama a la función main() al ejecutar el script