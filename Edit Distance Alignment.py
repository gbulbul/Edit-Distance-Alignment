# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:10:25 2024

@author: gbulb
"""

class Edit_Distance_Alignment:
    def protein_alignments_count(STRING_pretty,STRING_prttein):    
        counter=0
        for i in range(len(STRING_pretty)):
            if STRING_pretty[i]!=STRING_prttein[i]:
               counter+=1
        return print(counter)
    def protein_alignments(dict_):
        STRING_pretty=''
        STRING_prttein=''
        for value1 in dict_.values():
            for value2 in dict_.values():
                if value1!=value2:
                   for i in range(min(len(value1),len(value2))):
                       if value1[i]==value2[i]:
                          if value1[i] not in STRING_pretty:
                             STRING_pretty+=value1[i]
                             #print(f'STRING_pretty:{STRING_pretty}')
                          if value2[i] not in STRING_prttein:
                             STRING_prttein+=value2[i]
                             #print(f'STRING_prttein:{STRING_prttein}')
                       if value1[i]!=value2[i]:
                           if value1[i] not in STRING_pretty or value1[i:i+2] not in STRING_pretty:
                              STRING_pretty+=value1[i]
                              #print(f'STRING_pretty1:{STRING_pretty}')
                       
                   
                       if value1[i+3:]!=value2[i+3:]:
                            if value2[i] not in STRING_prttein:
                               STRING_prttein+='-'
                               
                   
                       if value1[:i+3]!=value2[:i+3]:
                            if value1[:i+2]!=value2[:i+2]:
                                 if value1[i]!=value2[i]:
                                    if value2[i] not in STRING_prttein:
                                       STRING_prttein+=value2[i:i+3]
                                       #print(f'STRING_prttein2:{STRING_prttein}')
                if len(value1)<len(value2):
                      STRING_pretty+='-'*(abs(len(value1)-len(value2))+1)
                     
                      return(STRING_pretty,STRING_prttein)
            
if __name__=="__main__":               
    dict_={}
    dict_['Rosalind_43']='PRETTY'
    dict_['Rosalind_97']='PRTTEIN'  
    STRING_pretty,STRING_prttein=Edit_Distance_Alignment.protein_alignments(dict_)
    Edit_Distance_Alignment.protein_alignments_count(STRING_pretty,STRING_prttein)
    print(STRING_pretty)
    print(STRING_prttein)
    