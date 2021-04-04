def solution(companies, applicants):
    company = []
    for c in range(len(companies)):
        company.append(companies[c][0])
    my_dict = {}
    pick = {} # '{A':['f', 'b'] 'B':['c', 'e'] 'C':['e', 'c'] }
    conclude = {}
    for d in company:
        my_dict[d] = []
        pick[d] = []
        conclude[d] = []

    for i in range(len(applicants)):
        wants = int(applicants[i][-1])
        want_company = applicants[i][2:2+len(company)]
        for j in range(wants):
            my_dict[want_company[j]] += applicants[i][0]

    for i in range(len(companies)):
        com,com_want,person = companies[i].split()
        person = int(person) # 회사 인원 규모
        for peo in com_want:
            if peo in my_dict[com]:
                pick[com] += peo
                if len(pick[com]) == person:
                    break
    


    answer = []
    return answer


companies = ["A fabdec 2", "B cebdfa 2", "C ecfadb 2"]
applicants = ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]
solution(companies, applicants)