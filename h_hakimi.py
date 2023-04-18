# Estare implementando el algoritmo de Havel - Hakimi.
from graphic import ploting

class Problem:

    def __init__(self, sec_grades: list()):
        self.sec_grades = sec_grades
    
    def havel_hakimi(self):
        if sum(self.sec_grades) % 2 != 0:
            return ('The sequence doesn\'t satisfy Handshaking Theorem', False)
        
        while True:
            print(self.sec_grades)

            self.sec_grades.sort(reverse=True)
            deleted = self.sec_grades.pop(0)
            
            if deleted >= len(self.sec_grades):
                return ('The first grade is bigger than the number of vertex of the graph', False)
            
            for i in range(0, deleted):
                self.sec_grades[i] -= 1

            if set(self.sec_grades) == {0}:
                return ('The graph is graphic', True)

            breakable = len(list(filter(lambda grade: grade  < 0, self.sec_grades[:deleted])))
            
            if breakable > 0:
                return ('Contradiction ↯', False)

sec = [6, 6, 6, 6, 4, 3, 3, 0] # Clase
sec2 = [1, 4, 2, 4, 3, 2]      # Clase

problema = Problem(sec)
solution = problema.havel_hakimi()

print(f'{problema.sec_grades} - {solution}')

if solution[1]:
    answer = int(input('[+] Do you want to see it in a graph?  (press 0: yes - press 1: otherwise): '))
    if answer == 0:
        ploting(sec, solution)
    elif answer == 1:
        print('Thanks')
    else:
        print('Enter a valid option')
