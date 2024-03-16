import math
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


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def compute_length(self):
        return self.start.compute_distance(self.end)

    def compute_slope(self) -> float:
        if self.start.y == self.end.y:
            if self.start.x > self.end.x:
                return 180
            else:
                return 0
        elif self.start.x == self.end.x:
            if self.start.y > self.end.y:
                return 270
            else:
                return 90
        else:
            
            component_y = self.end.y - self.start.y
            component_x = self.end.x - self.start.x
            radians_slope = math.atan(component_y / component_x)
            return math.degrees(radians_slope)

    def compute_horizontal_cross(self) -> bool:
        if self.start.y <= 0 and self.end.y > 0 or self.end.y <= 0 and self.start.y > 0:
            return True
        else:
            return False



    def compute_vertical_cross(self) -> bool:
        if self.start.x <= 0 and self.end.x > 0 or self.end.x <= 0 and self.start.x > 0:
            return True
        else:
            return False


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
    
    
    def fourth_method(self, first_line: Line, second_line: Line, third_line: Line, fourth_line: Line):
        self.width = first_line.compute_length()
        self.height = second_line.compute_length()

        self.bottom_left = first_line.start
        self.top_right = third_line.end

    def are_valid_rectangle_lines(self, first_line: Line, second_line: Line, third_line: Line, fourth_line: Line) -> bool:
        
        if not (self.are_perpendicular(first_line, second_line) and
                self.are_perpendicular(second_line, third_line) and
                self.are_perpendicular(third_line, fourth_line)):
            return False

        
        length1 = first_line.compute_length()
        length2 = second_line.compute_length()
        length3 = third_line.compute_length()
        length4 = fourth_line.compute_length()

        return length1 == length3 and length2 == length4

    def are_perpendicular(self, line1: Line, line2: Line) -> bool:
        
        slope1 = line1.compute_slope()
        slope2 = line2.compute_slope()

    
        return slope1 + slope2 == 90 or slope1 + slope2 == 270

        



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
    def __init__(self, method: int = 1, side_length: float = 0, bottom_left: Point = None, top_right: Point = None):
        if method == 1:
            super().__init__(method=1, width=side_length, height=side_length, bottom_left=bottom_left)
        elif method == 2:
            super().__init__(method=2, width=side_length, height=side_length)
        elif method == 3:
            super().__init__(method=3, bottom_left=bottom_left, top_right=top_right)

        self.side_length = side_length

    def are_valid_square_points(self, point1: Point, point2: Point) -> bool:
        distancia1 = point2.x - point1.x
        distancia2 = point2.y - point1.y
        
        print(distancia1)
        print(distancia2)
        
        return distancia1 == distancia2


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
            print("4. cuatro lineas")

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
                print("/nVERIFICAR INTERFERENCIA DE PUNTO")
                point_x = float(input("Ingrese la coordenada x del punto: "))
                point_y =float(input("Ingrese la coordenada y del punto: "))
                if rectangle.compute_interference_point(Point(point_x, point_y)):
                    print("el punto esta adentro de la figura")
                else:
                    print("el punto NO esta adentro de la figura")
               
            elif rect_choice == 2:
                center_x = float(input("Ingrese la coordenada x del centro: "))
                center_y = float(input("Ingrese la coordenada y del centro: "))
                width = float(input("Ingrese el ancho del rectángulo: "))
                height = float(input("Ingrese la altura del rectángulo: "))
                rectangle = Rectangle(method=2)
                rectangle.second_method(center=Point(center_x, center_y), height=height, width=width)
                print(f"El perímetro del rectángulo es: {rectangle.compute_perimeter()}")
                print(f"El área del rectángulo es: {rectangle.compute_area()}")
                print("/nVERIFICAR INTERFERENCIA DE PUNTO")
                point_x = float(input("Ingrese la coordenada x del punto: "))
                point_y =float(input("Ingrese la coordenada y del punto: "))
                if rectangle.compute_interference_point(Point(point_x, point_y)):
                    print("el punto esta adentro de la figura")
                else:
                    print("el punto NO esta adentro de la figura")
                
            elif rect_choice == 3:
                bottom_left_x = float(input("Ingrese la coordenada x del vértice inferior izquierdo: "))
                bottom_left_y = float(input("Ingrese la coordenada y del vértice inferior izquierdo: "))
                top_right_x = float(input("Ingrese la coordenada x del vértice superior derecho: "))
                top_right_y = float(input("Ingrese la coordenada y del vértice superior derecho: "))
                rectangle = Rectangle(method=3)
                rectangle.third_method(bottom_left=Point(bottom_left_x, bottom_left_y), top_right=Point(top_right_x, top_right_y))
                print(f"El perímetro del rectángulo es: {rectangle.compute_perimeter()}")
                print(f"El área del rectángulo es: {rectangle.compute_area()}")
                print("/nVERIFICAR INTERFERENCIA DE PUNTO")
                point_x = float(input("Ingrese la coordenada x del punto: "))
                point_y =float(input("Ingrese la coordenada y del punto: "))
                if rectangle.compute_interference_point(Point(point_x, point_y)):
                    print("el punto esta adentro de la figura")
                else:
                    print("el punto NO esta adentro de la figura")
             
            elif rect_choice ==4:

                print("Ingrese las coordenadas para las cuatro líneas que formarán el rectángulo:")
                point1_x = float(input("Ingrese la coordenada x del primer punto de la línea superior: "))
                point1_y = float(input("Ingrese la coordenada y del primer punto de la línea superior: "))
                point2_x = float(input("Ingrese la coordenada x del segundo punto de la línea superior: "))
                point2_y = float(input("Ingrese la coordenada y del segundo punto de la línea superior: "))
                line1 = Line(Point(point1_x, point1_y), Point(point2_x, point2_y))

                point3_x = float(input("Ingrese la coordenada x del primer punto de la línea izquierda: "))
                point3_y = float(input("Ingrese la coordenada y del primer punto de la línea izquierda: "))
                point4_x = float(input("Ingrese la coordenada x del segundo punto de la línea izquierda: "))
                point4_y = float(input("Ingrese la coordenada y del segundo punto de la línea izquierda: "))
                line2 = Line(Point(point3_x, point3_y), Point(point4_x, point4_y))

                point5_x = float(input("Ingrese la coordenada x del primer punto de la línea inferior: "))
                point5_y = float(input("Ingrese la coordenada y del primer punto de la línea inferior: "))
                point6_x = float(input("Ingrese la coordenada x del segundo punto de la línea inferior: "))
                point6_y = float(input("Ingrese la coordenada y del segundo punto de la línea inferior: "))
                line3 = Line(Point(point5_x, point5_y), Point(point6_x, point6_y))

                point7_x = float(input("Ingrese la coordenada x del primer punto de la línea derecha: "))
                point7_y = float(input("Ingrese la coordenada y del primer punto de la línea derecha: "))
                point8_x = float(input("Ingrese la coordenada x del segundo punto de la línea derecha: "))
                point8_y = float(input("Ingrese la coordenada y del segundo punto de la línea derecha: "))
                line4 = Line(Point(point7_x, point7_y), Point(point8_x, point8_y))


                rectangle = Rectangle()
                if not rectangle.are_valid_rectangle_lines(line1, line2, line3, line4):
                    print("Las líneas no forman un rectángulo válido.")
                    continue
                rectangle.fourth_method(line1, line2, line3, line4)

                print(f"El perímetro del rectángulo es: {rectangle.compute_perimeter()}")
                print(f"El área del rectángulo es: {rectangle.compute_area()}")
                print("/nVERIFICAR INTERFERENCIA DE PUNTO")
                point_x = float(input("Ingrese la coordenada x del punto: "))
                point_y =float(input("Ingrese la coordenada y del punto: "))
                if rectangle.compute_interference_point(Point(point_x, point_y)):
                    print("el punto esta adentro de la figura")
                else:
                    print("el punto NO esta adentro de la figura")
     
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
                print("/nVERIFICAR INTERFERENCIA DE PUNTO")
                point_x = float(input("Ingrese la coordenada x del punto: "))
                point_y =float(input("Ingrese la coordenada y del punto: "))
                if square.compute_interference_point(Point(point_x, point_y)):
                    print("el punto esta adentro de la figura")
                else:
                    print("el punto NO esta adentro de la figura")
            elif square_choice == 2:
                center_x = float(input("Ingrese la coordenada x del centro: "))
                center_y = float(input("Ingrese la coordenada y del centro: "))
                side_length = float(input("Ingrese la longitud del lado del cuadrado: "))
                square = Square(method=2, side_length=side_length)
                square.second_method(center=Point(center_x, center_y), height=side_length, width=side_length)
                print(f"El perímetro del cuadrado es: {square.compute_perimeter()}")
                print(f"El área del rectángulo es: {square.compute_area()}")
                print("/nVERIFICAR INTERFERENCIA DE PUNTO")
                point_x = float(input("Ingrese la coordenada x del punto: "))
                point_y =float(input("Ingrese la coordenada y del punto: "))
                if square.compute_interference_point(Point(point_x, point_y)):
                    print("el punto esta adentro de la figura")
                else:
                    print("el punto NO esta adentro de la figura")
            elif square_choice == 3:
                bottom_left_x = float(input("Ingrese la coordenada x del vértice inferior izquierdo: "))
                bottom_left_y = float(input("Ingrese la coordenada y del vértice inferior izquierdo: "))
                top_right_x = float(input("Ingrese la coordenada x del vértice superior derecho: "))
                top_right_y = float(input("Ingrese la coordenada y del vértice superior derecho: "))

                square = Square(method=3, bottom_left=Point(bottom_left_x, bottom_left_y), top_right=Point(top_right_x, top_right_y))
                square.third_method(bottom_left=Point(bottom_left_x, bottom_left_y), top_right=Point(top_right_x, top_right_y))
             
 
                if not square.are_valid_square_points(Point(bottom_left_x, bottom_left_y), Point(top_right_x, top_right_y)):
                    print("Los puntos ingresados no forman un cuadrado válido.")
                    continue

                print(f"El perímetro del cuadrado es: {square.compute_perimeter()}")
                print(f"El área del rectángulo es: {square.compute_area()}")
                print("/nVERIFICAR INTERFERENCIA DE PUNTO")
                point_x = float(input("Ingrese la coordenada x del punto: "))
                point_y =float(input("Ingrese la coordenada y del punto: "))
                if square.compute_interference_point(Point(point_x, point_y)):
                    print("el punto esta adentro de la figura")
                else:
                    print("el punto NO esta adentro de la figura")
                  
            else:
                print("Opción no válida")           
                continue
        elif main_choice == 3:
            break
        else:
            print("Opción no válida")






if __name__ == "__main__":
    main()
