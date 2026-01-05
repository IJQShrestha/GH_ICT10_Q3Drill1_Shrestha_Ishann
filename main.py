from pyscript import document, display

subs = ["Science","Math","English","Filipino","ICT","PE"]
unitss = (5,5,5,3,2,1)

def calculate_gwa(e):

    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    g1 = float(document.getElementById("science").value)
    g2 = float(document.getElementById("math").value)
    g3 = float(document.getElementById("english").value)
    g4 = float(document.getElementById("filipino").value)
    g5 = float(document.getElementById("ict").value)
    g6 = float(document.getElementById("pe").value)

    allgrades = [g1, g2, g3, g4, g5, g6]

    tot_units = sum(unitss)
    wsum = 0
    for i in range(len(subs)):
        wsum = wsum + (allgrades[i] * unitss[i])

    gwa = wsum / tot_units

    if gwa > 74:
        passed = "YES"
    else:
        passed = "NO"

    result = f"""
    <h4>Name: {fname} {lname}</h4>
    <br>
    {subs[0]}: {g1}<br>
    {subs[1]}: {g2}<br>
    {subs[2]}: {g3}<br>
    {subs[3]}: {g4}<br>
    {subs[4]}: {g5}<br>
    {subs[5]}: {g6}<br>

   
    <br>
    <b>Your general weighted average is: {gwa:.2f}</b>
    <br>
    <b>Passed?: {passed} </b>
    """
  
    
    out = document.getElementById("output")
    out.innerHTML = result