class Point:
    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y

    def reset(self):
        self.x = 0
        self.y = 0

    def compute_distance(self, point) -> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance

'''
class Line:
    def _init_(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def compute_lenght(self):
        return self.start.compute_distance(self.end)

    def compute_slope(self) -> float:
        return (self.start.y - self.end.y) / (self.start.x - self.end.x)

    def compute_horizontal_cross(self) -> bool:



    def compute_vertical_cross(self) -> bool:
'''

class Rectangle:

    def __init__(self, method: int = 1, width: float = 0, height: float = 0 , bottom_left: Point = None , top_right: Point = None): 
        self.width = width
        self.height = height
        self.method = method
        self.bottom_left = bottom_left
        self.top_right = top_right
    
    def first_method(self, bottom_left: Point, height: float = 0, width: float = 0):
        self.height = height
        self.width = width
        self.bottom_left = bottom_left
        self.top_right = Point((bottom_left.x + width), (bottom_left.y + height))
    
    def second_method(self, center: Point = None , height: float = 0, width: float = 0):
        self.height = height
        self.width = width
        self.bottom_left = Point((center.x - (width/2)), (center.y - (height/2)))
        self.top_right = Point((center.x + (width/2)), (center.y + (height/2)))
        
    def third_method(self, bottom_left: Point = None, top_right: Point = None):
        self.height = (top_right.y - bottom_left.y)
        self.width = (top_right.x - bottom_left.x)
        self.bottom_left = bottom_left
        self.top_right = top_right
        



    def compute_area(self):
        return self.height * self.width

    def compute_perimeter(self):
        return (2*(self.height))+(2*(self.width))

    def compute_interference_point(self, point: Point):
        if point.x < self.bottom_left.x or point.x > (self.bottom_left.x + self.width):
            return False
        elif point.y < self.bottom_left.y or point.y > (self.bottom_left.y + self.height):
            return False
        else:
            return True
        


class Square(Rectangle):
    def __init__(self, method: int = 1, side_length: float = 0, bottom_left: Point = None, center: Point = None, top_right: Point = None):
        if method == 1:
            super().__init__(method=1, width=side_length, height=side_length, bottom_left=bottom_left)
        elif method == 2:
            super().__init__(method=2, width=side_length, height=side_length, center=center)
        elif method == 3:
            super().__init__(method=3, bottom_left=bottom_left, top_right=top_right)

        self.side_length = side_length

    def are_valid_square_points(point1: Point, point2: Point) -> bool:
        
        side_length = abs(point1.x - point2.x)
        if abs(point1.y - point2.y) != side_length:
            return False

        
        if point1.x == point2.x or point1.y == point2.y:
            return True
        else:
            return False





def main():
    while True:
        print("\nOpciones:")
        print("1. Crear Rectángulo")
        print("2. Crear Cuadrado")
        print("3. Salir")

        main_choice = int(input("Ingrese el número de la opción: "))
        if main_choice == 1:
            print("\nOpciones:")
            print("1. Vértice inferior izquierdo + ancho y alto")
            print("2. Centro + ancho y alto")
            print("3. Vértice inferior izquierdo y vértice superior derecho")

            rect_choice = int(input("Ingrese el número de la opción: "))
            if rect_choice == 1:
                bottom_left_x = float(input("Ingrese la coordenada x del vértice inferior izquierdo: "))
                bottom_left_y = float(input("Ingrese la coordenada y del vértice inferior izquierdo: "))
                width = float(input("Ingrese el ancho del rectángulo: "))
                height = float(input("Ingrese la altura del rectángulo: "))
                rectangle = Rectangle(method=1)
                rectangle.first_method(bottom_left=Point(bottom_left_x, bottom_left_y), height=height, width=width)
                print(f"El perímetro del rectángulo es: {rectangle.compute_perimeter()}")
                print(f"El área del rectángulo es: {rectangle.compute_area()}")
                break
            elif rect_choice == 2:
                center_x = float(input("Ingrese la coordenada x del centro: "))
                center_y = float(input("Ingrese la coordenada y del centro: "))
                width = float(input("Ingrese el ancho del rectángulo: "))
                height = float(input("Ingrese la altura del rectángulo: "))
                rectangle = Rectangle(method=2)
                rectangle.second_method(center=Point(center_x, center_y), height=height, width=width)
                print(f"El perímetro del rectángulo es: {rectangle.compute_perimeter()}")
                print(f"El área del rectángulo es: {rectangle.compute_area()}")
                break
            elif rect_choice == 3:
                bottom_left_x = float(input("Ingrese la coordenada x del vértice inferior izquierdo: "))
                bottom_left_y = float(input("Ingrese la coordenada y del vértice inferior izquierdo: "))
                top_right_x = float(input("Ingrese la coordenada x del vértice superior derecho: "))
                top_right_y = float(input("Ingrese la coordenada y del vértice superior derecho: "))
                rectangle = Rectangle(method=3)
                rectangle.third_method(bottom_left=Point(bottom_left_x, bottom_left_y), top_right=Point(top_right_x, top_right_y))
                print(f"El perímetro del rectángulo es: {rectangle.compute_perimeter()}")
                print(f"El área del rectángulo es: {rectangle.compute_area()}")
                break
            else:
                print("Opción no válida")
        elif main_choice == 2:
            print("\nOpciones:")
            print("1. Vértice inferior izquierdo + lado")
            print("2. Centro + lado")
            print("3. Vértice inferior izquierdo y vértice superior derecho")
            
            square_choice = int(input("Ingrese el número de la opción: "))
            if square_choice == 1:
                bottom_left_x = float(input("Ingrese la coordenada x del vértice inferior izquierdo: "))
                bottom_left_y = float(input("Ingrese la coordenada y del vértice inferior izquierdo: "))
                side_length = float(input("Ingrese la longitud del lado del cuadrado: "))
                square = Square(method=1, side_length=side_length, bottom_left=Point(bottom_left_x, bottom_left_y))
                print(f"El perímetro del cuadrado es: {square.compute_perimeter()}")
                print(f"El área del rectángulo es: {square.compute_area()}")
            elif square_choice == 2:
                center_x = float(input("Ingrese la coordenada x del centro: "))
                center_y = float(input("Ingrese la coordenada y del centro: "))
                side_length = float(input("Ingrese la longitud del lado del cuadrado: "))
                square = Square(method=2, side_length=side_length, center=Point(center_x, center_y))
                print(f"El perímetro del cuadrado es: {square.compute_perimeter()}")
                print(f"El área del rectángulo es: {square.compute_area()}")
            elif square_choice == 3:
                bottom_left_x = float(input("Ingrese la coordenada x del vértice inferior izquierdo: "))
                bottom_left_y = float(input("Ingrese la coordenada y del vértice inferior izquierdo: "))
                top_right_x = float(input("Ingrese la coordenada x del vértice superior derecho: "))
                top_right_y = float(input("Ingrese la coordenada y del vértice superior derecho: "))
             
 
                if not Square.are_valid_square_points(Point(bottom_left_x, bottom_left_y), Point(top_right_x, top_right_y)):
                    print("Los puntos ingresados no forman un cuadrado válido.")
                    continue
                
                square = Square(method=3, bottom_left=Point(bottom_left_x, bottom_left_y), top_right=Point(top_right_x, top_right_y))
                print(f"El perímetro del cuadrado es: {square.compute_perimeter()}")
                print(f"El área del rectángulo es: {square.compute_area()}")                  
            else:
                print("Opción no válida")           
                continue
        elif main_choice == 3:
            break
        else:
            print("Opción no válida")






if __name__ == "__main__":
    main()