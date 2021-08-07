entree = """
somme = 0
mult = 1
for nb in range(10):
    somme += nb
    if somme > 3:
        mult *= nb ** 2
    else:
        mult += nb
print(somme)
print(mult)
"""
avant,apres,boucle1,corps="","","",""
bcl_var,bcl_indt="",4
r_debut,r_inc,r_fin=0,1,0
idx_actu=0
mot_prec,mot_actu="",""
dans_boucle1,dans_corps,dans_r,debut_l=False,False,False,True
verifie_mot_prec=False
for c in entree:
    if c not in {",",":","(",")",";","\n"," ","=","<",">","{","}","[","]","+","-","*","/","%","#","\t","\r","\"","\'"}:
        mot_actu += c
    elif mot_actu != "":
        mot_prec,mot_actu,verifie_mot_prec=mot_actu,"",True
    if c == "\n":
        idx_actu,debut_l=0,True
        if dans_boucle1:
            dans_boucle1,dans_r,dans_corps=False,False,True
    else:
        if c == " ":
            if debut_l:idx_actu+=1
        else:
            debut_l=False
            if dans_corps and idx_actu<bcl_indt+4:dans_corps=False
    if verifie_mot_prec:
        if mot_prec == "for":dans_boucle1,bcl_indt,avant,boucle1=True,idx_actu,avant[:-3],"for"
        elif dans_boucle1 and len(bcl_var)==0:bcl_var=mot_prec
        elif dans_boucle1 and mot_prec == "range":dans_r=True
        elif dans_r:r_fin=int(mot_prec)
        mot_prec,verifie_mot_prec="",False
    if dans_corps:corps+=c
    elif dans_boucle1:boucle1+=c
    elif len(boucle1)==0:avant+=c
    else:apres+=c
final_code,lines=avant,corps.split("\n")
for i in range(r_debut,r_fin,r_inc):
    for line in lines:
        if len(line)>4:final_code+=line[4:].replace(bcl_var,str(i))+"\n"
final_code+=apres
print(final_code)