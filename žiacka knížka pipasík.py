import turtle

root = turtle.Screen()
p = turtle.Turtle()
root.setup(500,350)
turtle.title("low budget EDUPAGE")
turtle.bgcolor("black")

p.pen(pencolor="white",speed =0)
p.hideturtle()
p.up()
p.goto(95,-165)
p.write("Code written by Peter Pipasík")

font_na_pisanie = ("calibri 15")

vsetky_znamky = []

x,y = (-200,100)

kolko_znamok = int(root.textinput(" ","Zadajte počet známok"))
if kolko_znamok < 1:
    exit()

for znamky_cyklus in range(int(kolko_znamok)):
    znamky_zadavanie = int(root.textinput(" ",("Zadajte",int(znamky_cyklus+1),"známku")))
    if znamky_zadavanie > 5 or znamky_zadavanie < 1:
        zle_zadanie_znamky = int(root.textinput("Neplatná známka","Prosím zadajte platnú známku (od 1-5) \ninak budete odhlásený"))
        if zle_zadanie_znamky > 5 or zle_zadanie_znamky < 1:
            exit()
        vsetky_znamky.append(int(zle_zadanie_znamky))
    vsetky_znamky.append(znamky_zadavanie)
    if znamky_zadavanie > 5 or znamky_zadavanie < 1:
        vsetky_znamky.remove(znamky_zadavanie)

priemer_znamok = round(((sum(vsetky_znamky))/kolko_znamok),2)

# kvoli zlemu zaokruhlovaniu tu je tento test cisel
if priemer_znamok == 1.5:
    vysledna_znamka = 1
elif priemer_znamok == 2.5:
    vysledna_znamka = 2
elif priemer_znamok == 3.5:
    vysledna_znamka = 3
elif priemer_znamok == 4.5:
    vysledna_znamka = 4
else: 
    vysledna_znamka = round(priemer_znamok)

p.goto(x,y)
p.write("Vaše známky sú: " + str(', '.join(map(str, vsetky_znamky))) ,font=font_na_pisanie)
p.goto(x,y-40)
p.write("Váš priemer je: " + str(priemer_znamok),font=font_na_pisanie)
p.goto(x,y-80)
p.write("Výsledná známka je: "+ str(vysledna_znamka),font=font_na_pisanie) 


root.mainloop()