class Solution(object):
    def scheduleCourse(self, courses):
        lista = self.merge(courses)
        print(lista)

        tempo = 0
        conta = 0
        tarefas_realizadas = []

        while len(lista)>0:
            aux = lista[0]
            lista.remove(aux)
            tempo+=aux[0]
            if(tempo <= aux[1]):
                tarefas_realizadas.append(aux)
                conta+=1
        print(conta)

        return conta

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

        while i<len(esquerda) and j<len(direita):
            if esquerda[i][1] <= direita[j][1]:
                lista_ordenada.append(esquerda[i])
                #print(esquerda[i], esquerda[i][1])
                i+=1
            elif esquerda[i][1] > direita[j][1]:
                lista_ordenada.append(direita[j])
                #print(direita[j], direita[j][1])
                j+=1

        lista_ordenada.extend(esquerda[i:])
        lista_ordenada.extend(direita[j:])   

        return lista_ordenada     

entrada = [[3,2],[4,3]]

tarefas = Solution()

resultada = tarefas.scheduleCourse(entrada)

print(resultada)