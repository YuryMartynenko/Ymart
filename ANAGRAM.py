#ANAGRAMM
def anagram(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    res = 0
    for i in range(len(s1)):
        if s2[i] == s1[i]:
            res += 1
            if res == len(s2):
                return 'Введённые строки являются анаграммой.'
    else:
        return 'Вторая строка не является анаграммой первой строки.'


word_input1 = input('Введите слово : ')
word_input2 = input('Введите тоже самое слово, буквами в обратном порядке : ')
result = anagram(word_input1, word_input2)
print(result)
        
    
    
    
    
    
