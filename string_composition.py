# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:38:07 2016

@author: fang2
"""
def radixSortFixedString(array):
    fixedLength=len(array[0])
    oa=ord('A')
    oz=ord('Z')
    n=oz-oa+1
    buckets = [[] for i in range(0,n)]
    for position in reversed(range(0,fixedLength)):
        for string in array:
            buckets[ord(string[position])-oa].append(string)
        del array[:]
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]

    return array


def string_composition(k,text):
    if k>len(text):
        print("the window length is larger than the text length")
        raise IndexError
    result=[]    
    for i in range(len(text)-k+1):
        result.append(text[i:i+k]) 
    
    result=radixSortFixedString(result)
    return result
    
def get_prefix(string):
    length=len(string)
    prefix=string[0:length-1]
    return prefix

def get_suffix(string):
    suffix=string[1:len(string)]
    return suffix

def get_overlap_graph(Input):
    temp=Input
    graph=[[] for _ in range(len(Input))]
    for i in range(len(Input)):
        for j in range(len(temp)):
            if get_suffix(Input[i])==get_prefix(temp[j]):
                graph[i].append(1)
            else:
                graph[i].append(0)
    
    return graph

    
        
        
text="GACAACATTATCGATTCTAAGAACCATGGATGAATACCAGGTTCTGCCAATCGATAAAGTCGCCGACACGCGCGTCCTGGCACAACAGTGCGTCTCATGATTTGGTGGTAGCATTTACGTTAGGAACAGTTTTTAACCGGTGCCGGCGCCGTGGTTCGGACGCGAGTAGTTCTCTTCTTGGAGCCTCGTATCCTAGCAATAAAAGGGCGCGAAGGTTTCGGATGATAATCATGAGCCAGTACACTGTTGCAGGCAGGTCCCTCACACGACAGGCAATTGGGTAGATGTCGGTTAGACTCCGCAGACTGTGTTAGAGGCACGCCTACTGGATTCCAGTGACGGCTAGTTATTGTCTCTGGGCTGACCGTGGACAAGCACGGTATCAGATACCGCAACTCGAATCATAACCGATCGACGCCAAAATACATTCACAATGTAGTTTGGATTAACCAGGACTTCGGGGTGAGATTTGGCCGCCCAGGAAAAGATATAGGGGGGAATGACCGTAAAGTGTGCGCGGCTCACGCAGTACCAGCCTTACCCTGATAATTCGAACCCTACCAGAGGTGCCAAATGCAATATTAATCCGACAAGTCTCCTTAGGGTAGTCCTACGTTAAACTGACTGCCGGTGCCCGGTGGGGGCACGCTAATAGTCCCCTATCTGGGGTTCTCCACGTCACATAACACCTGCTTCTAAGTCATAGTGTCCAACCTGCACATGACAGTAACCTACATTCAGAGACTTGATAATCTCGTCTGGACTGGCAAAAGCGTAGGTAATGGCCCGCAGTTAAAACGTTATGACATCTCATTGTATAACAAAATCGAAGTGCAAATCCTTGAGTCCCGTTGTTTCAATACAACCAGCCTTAGCGGGAGGTAAGCGTTCTCTTGTTGATCTCTTGGTTGAGCGTCCGGGCCCGGTATGCTTGTACCCTCTTATAATGAACTTTAAGCAGGTGAGCGATGAACTTCCTCCTGTCTAATCTCATCAAGCCATGACCGAGGCCCGGTTTGCAGTAAAACCAAAAGACGGTTGAGTAGCGAAGGAAATGATGTGCGCGAGGTGGTGCTAACCATGCTCTGTACGTCGCGTGCCTTTGATGGCGTGTGTAAACTTGCGACGATATTTCAGAGTTGAACATTTACCGTAAATGCTGCGGGACGAGCGATGGGCACATGCGCTTGAAGTGGTGGAGCAACAGCCGAATAGGTGACGTGATCCTGCGTTTACTTGTCAACTGCATCCGGTATCCCTGCTAAGACTAACGTCACTTCATGGCAGCCCCTGATCTTTCCTACCCCTGTATGTTGACCAACGTACGTGGACAATGAGGTCCACTCATAGCCCAGAGTACAGTTGAGGTCGCACGCCAGGAAGCGCCTACGCTACTTAAAGCCCTTGATCCCCGGCGTTTTAAGCACCTACTATCTCGCTGAGCCCCACTCCGTACAATAACTTCAGTTCATTTCCAGTAAACTACCATGCCTCTCAAATATCGAGTACTACCGGCTAGAGGACTAATCAGGATATAATAAAACGTCGGGACGAAAGGCCAGGACGCCGCAAATCCATACCGCGGCATGAGGGTCTGCCATCCACGCTTCGCGATGGCTGGGAAATGGACATCTTATAACGTTACTCCCTAGGGCCCTAGGGCAAGATATTATCTTTATGTGACATGGTAGGAACATGGATCCGCGCTGTGGATTCCACAGAGGATAGGAGTGAGTTGGAAGTCTAGTGATTTTTTCAAGGAGCGGAGCAGGGAAAATCTCCGGCAGATCCTTTGTCCATCTGTCGCCTAATTGTATCCGAATGTTATAAGAGAACAGTAAAGGAAGTTCTTTATGGATTGCGCGGTGAATAAGCAGCCGGGATGCGCTAGAGCACCTCTGATGACACGGTCACCTAGTCGGCTCGGGAACCTTAGATATTTTACGTTTTTCTGCTAGACACCATTGCGGGCGGATACTTCGGACACGCAGGGTTAGGTGCCCGAGCCATTTGGGCTATGCGGTACTCCGGCACTAATATCTTTATGTTGGCTGTACGATGAGTCGACACCGAGCCGTATGCAGATATTTCCATATACGCATGATCGTTCGCATGTATCCCAACGCACAACAGGTGCCTGAAATCGACAGCATCGCCTGGGAATCTCCTTAAGGGGCGTGGCAACGACATGTGCAGTCTAGTACGACTGGTGCGGCCGTTATTTATGACGGAAATCGGGTGACCAGCGGGGTTGGAGTGCTTCGTCACATTTTGGCACTGACGGGTTTAAAGTACGCCCGTCTGGGGAGTTCAGCGTACACTAGGGACACGCATTGTGCAGCTAAACGCCCGTTGAGTAACTTGACCTCGCTCTGGCTCATCGTAACCACCATGCATATAGAAAAGAGCTTGGTCAGACAAAATCAGAAAAAGGCGCGAGACATTGTTATAGAATGTATGTTTCGCATGGGTGCGCTTTTAGCGCTTCCTCTCCAGGATAGACAGACGCTAAAATCAACATAACGGTAATGGGCCACGTATAAATATCCAAAACGATGCAACGAGCACGTTCGCTTCAGCCCGGGGCCCACCACATGTTTGAGATATGCTTGTCTCTCATTAGAATAGTAACCGTTTGCTGTTCCGTGTTCAGTCCCACTTATTAATTGTGAGTCGCGTAGCGCCATCTATTTCTAGAATGAAGTGGTGCCCATTCCAGCGCAACTATACACGAGCAAAAGCGGCGCTTAGCCCGTCCTCTGCGGGGCTCAAACCGCCCTATATTCTTGGCCTTGCCCCTTCACCAGATGGAATCGACCACATCGCATCTCGTAATCCACTCTAGGCGCGTGAGCACCGTCCTATGATGTGTTTCGAGGCTGTTGACGATCGAGATAGCTGATATGGAATTACGTCCTAGCCGCTTCGAGGCGGTGGCAGCTGATTGTCGATCGGCGTAGGATCCTCGGCTACACCAATCCTATACGTGATTGTAATCGGATGCTCCCGGGGGTGTTATGAGATGTTTTTCGCATATCGCTAGGTAGGGCCGCACTGCTGGGGATGTTACACAGCTCCTACCAGTGTCATACAACACGCTAGCTGTAGCGGGAATACCCCTTGATTTCTGATCGCGTCCCCCTTATGGTTAACGTGGGCCGTATACCGCACAGTCGATGCCTTGATGGGATTAATCAAATCTTTTGACTAGATCATTGCATCCGTAAGCTCAAATACAGCTAGGGACTTCCTCTGTACTCAGGGTAGGCTCAAGCTCACAACTCATCTTGGGGCACATCGATGTGGTGCTGATCACACAGTGCGGTGTGGGTTTGCGTCGTACGCCCTCTTCTGGTACTCAGTGGAGCGTAAGGTTTGGTCGATGACACCGGAACAGAAGATTCGACATAAGGTAGAGAGACTTCAAACCTCGGGCAGGTGAAAACGCTCCCGGGGGCGGCTGGATAAGGTTAGTCGGCTAAGGGCAAATACATACCTAACGTTCCCGATTGTACAAGAGTAGAAAGGGACAATTAATGTAAGAGTTACATCTCCCAAAGTAATGTAAATGCCTAGGAGTCATCAAGTGACTTTCGATCAAGACTATAATCACTCCGTGCTCAACAACTGTATTGCGCTTAAGCCTCCAGGTAAGGCTAATGTTGTCACAGAACTGACAAGGGACTTGTTATCCGACTTCTGTAAAAGGGGCATCTTGGGCTCAGCACAGTCGCTCGAATGTCGGCTATACAGTTTAACGACGTCGCCGCGTTAAAACACAAGGGATTCTCTTCGTAATATTCAGGGTGTGTCTCAGTATGAAGTGGCCCATTCCAATCGAGGTGCCACTGCCGGTCCTGACCATGCCACCTTCAAGCTTCCAAACTTCGGCCTCACGATATAATTCATGATCGGTCAACACGTGCGGCATCCAGTGTCTTAGATTCGGGAAAAAGTCTACATTGGCGCGGTCCGTACGACCCTCCTACGCACGCTGACAAGCACACCTATGCAAGTCCTTAACGCCTTTCCGCCCACGTGGGCCGTAGGGCGTGTGTGCCACTAATGGGTCTAGCACTTATATGTCGCGTTGATGAGCTCCAGAGTTTCAGTTCCAGGTTAACTTGGGTATTGCTGTCGTTATGCAGTATGGAGGATCTACGATAGTAAAACATGTGAATTCAGGATGAGTTGTCTGTAGAAGCGTATGAGCAAGTAATCGTAATGTTGGGTGGTTCCCCTCTTAAAACCTAATTTGGCGGGCCGCGCTGGCGCGTCATCTTCTTCTGCCACGTATCGGTAAATTTAGTGACATTGCTTTTTTGTGTGGAGTCACCAGTGATCGTACACCGGTAATAAAACGTGGAGCATTCGGTGGCTTGGGTATGCTAGGCATCTGCGAGCCATCCGAGAGCTATCAGCCAATACTTTCGCACAAGTCGCACTAATGAATCTAGGAGGGGAGTATTAGGTCCGGAAATGGGCCGAAAGCACTAGTTAGATCAGTACGGAGCTGTGGAACAGGGAACCTTACGACCTGGGTGCTTAAGATGTCAACATATCATGTCCGTCTTATAGATCAATGAACGGCGACGGAAAATTACCCAGAGGTCCTCGGTTGTTAGCCGGGATCAAAGTGTACACATTGTAAGCCAGGCCCGACCAATATGTTCACAAGATGACGTAGCGCGGCGTTGCAGAGCACCGCTGCTGGTCGTCCCCCAATAGGCGCCTTAAGAGGCCTCTACCAGGCAAGAGAATCTGGAGTTGTCTTAGTCGCGATAAAGGAATCCGTGGTTGAGTACCCCGGAAGTTTTAATGGGGTAACGGTGTTTGCGACCGCGCCGACCTCACCAGGTCCGTCTATATTAAGTGGGCGTGTGTTCCTCAACCCTGATTCAGTGACCGCTCTACCCTACCTATTAACACAGAATAGCTCGAACGACGCGAGCGCGCAGAGGATCTTTATTTCTACATTGTGCCGACACCCCCCGGAAGGA"
result=string_composition(100,text)
test=["ATGCG","GCATG","CATGC","AGGCA","GGCAT"]
graph=get_overlap_graph(result)
a=[]
for i in range(len(graph)):
    a.append(graph[i].index(1))
            
        