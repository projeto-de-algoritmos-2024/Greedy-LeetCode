import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        # Ordena os cursos por prazo de entrega crescente
        courses = self.merge(courses)

        tempo = 0
        heap = []

        for duracao, prazo in courses:
            if tempo + duracao <= prazo:
                # Adiciona a tarefa ao heap e atualiza o tempo
                heapq.heappush(heap, -duracao)  
                tempo += duracao
            elif heap and -heap[0] > duracao:
                # Substitui a tarefa mais longa por uma tarefa mais curta
                tempo += duracao - (-heapq.heappop(heap))
                heapq.heappush(heap, -duracao)

        return len(heap)  


    def merge(self, lista):
        if len(lista)<=1:
            return lista
    
        
        meio = len(lista)//2

        esquerda = lista[:meio]
        direita = lista[meio:]

        esquerda_ordenada = self.merge(esquerda)
        direita_ordenada = self.merge(direita)

        lista_ordenada = self.merge_union(esquerda_ordenada, direita_ordenada)

        return lista_ordenada

    def merge_union(self, esquerda, direita):
        i=0
        j=0

        lista_ordenada = []

        # while i<len(esquerda) and j<len(direita):
        #     if esquerda[i][0] + esquerda[i][1] < direita[j][0] + direita[j][1]:
        #         lista_ordenada.append(esquerda[i])
        #         #print(esquerda[i], esquerda[i][1])
        #         i+=1
        #     elif esquerda[i][0] + esquerda[i][1] > direita[j][0] + direita[j][1]:
        #         lista_ordenada.append(direita[j])
        #         #print(direita[j], direita[j][1])
        #         j+=1
        #     elif esquerda[i][0] + esquerda[i][1] == direita[j][0] + direita[j][1]:
        #         if esquerda[i][0] < direita[j][0]:
        #             lista_ordenada.append(esquerda[i])
        #             #print(esquerda[i], esquerda[i][1])
        #             i+=1
        #         elif esquerda[i][0] > direita[j][0]:
        #             lista_ordenada.append(direita[j])
        #             #print(direita[j], direita[j][1])
        #             j+=1
        #         elif esquerda[i][1] < direita[j][1]:
        #             lista_ordenada.append(esquerda[i])
        #             #print(esquerda[i], esquerda[i][1])
        #             i+=1
        #         elif esquerda[i][1] > direita[j][1]:
        #             lista_ordenada.append(direita[j])
        #             #print(direita[j], direita[j][1])
        #             j+=1


        while i<len(esquerda) and j<len(direita):
            if esquerda[i][1] < direita[j][1]:
                lista_ordenada.append(esquerda[i])
                #print(esquerda[i], esquerda[i][1])
                i+=1
            elif esquerda[i][1] > direita[j][1]:
                lista_ordenada.append(direita[j])
                #print(direita[j], direita[j][1])
                j+=1
            else:
                if esquerda[i][0] <= direita[j][0]:
                    lista_ordenada.append(esquerda[i])
                    #print(esquerda[i], esquerda[i][1])
                    i+=1
                else:
                    lista_ordenada.append(direita[j])
                    #print(direita[j], direita[j][1])
                    j+=1

        lista_ordenada.extend(esquerda[i:])
        lista_ordenada.extend(direita[j:])   

        return lista_ordenada     

entrada = [[5,5],[4,6],[2,6]]

tarefas = Solution()

resultada = tarefas.scheduleCourse(entrada)

print(resultada)