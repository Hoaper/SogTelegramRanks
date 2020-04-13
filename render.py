def save(sid, rank, color):
    try:
        with open('custom-chatcolors.cfg') as file:
            #Получяем чисто тело
            content = file.readlines()[2:-1]
            newUser = '\t"%s"\n\t{\n\t\t"tag" "{%s}[%s]"\t\n\t}'%(sid, color, rank[0])
            add = "admin_colors\n{\n" + ''.join(content) + newUser + '\n}'
        # Запись в config
        with open('custom-chatcolors.cfg', 'w') as f:
            f.write(add)
        return True
    except Exception:
        return False