import heapq   

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        qualidade_total = 0
        meu_custo = 1000000000000000
        razao_qual_wage = []
        # aqui adicionamos a razao salario/qualidade a uma lista de tuplas.
        for i in range(len(wage)):
            aux = float(wage[i]/quality[i])
            razao_qual_wage.append((aux,quality[i]))

        # ordenamos a lista em ordem crescente de razao
        razao_qual_wage.sort(key= lambda par: par[0]) 
        maxheap = []

        # percorrer todas as tuplas em razao_qual_rage
        for razao, qualidade in razao_qual_wage:
            
            # adicionamos -qualidade para criar uma logica de maxheap em vez de minheap
            heapq.heappush(maxheap, -qualidade)
            # somamos a qualidade da tupla que estamos analisando em qualidade_total
            qualidade_total += qualidade

            # mantemos apenas k funcionarios na heap, se k eh ultrapassado, tiramos o funcionario de maior razao da heap
            if len(maxheap) > k:
                # e aqui removemos a qualidade dele de qualidade total
                qualidade_total += heapq.heappop(maxheap)

            # se chegamos a quantidade k de funcionarios que precisamos contratar
            if len(maxheap) == k:
                # fazer a analise de custo minimo: compara o custo da iteracao anterior (que chegou em k) com o custo que tenho agora e pega o menor valor
                meu_custo = min(meu_custo, razao * qualidade_total)

        # arredondando pois o problema quer com 5 casas decimais
        return round(meu_custo,5)
        


def main():

    quality = [3,1,10,10,1]
    wage = [4,8,2,2,7]
    k = 3
    minimum = Solution()
    
    print(minimum.mincostToHireWorkers(quality,wage,k))


main()