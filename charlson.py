def mapear_charlson(icd9_list):
    categorias = set()
    for code in icd9_list:
        code = str(code).replace('.', '').strip()
        if not code.isdigit():
            continue

        code_int = int(code[:3])  # usa os 3 primeiros dígitos

        # 1. Doença cardíaca congestiva
        if code.startswith('428'):
            categorias.add('CHF')

        elif code_int in range(440, 445) or code.startswith('0930') or code.startswith('7854') or code.startswith('V434'):
            categorias.add('PVD')

        # 3. Doença cerebrovascular
        elif code_int in [430, 431, 432, 433, 434, 435, 436, 437, 438]:
            categorias.add('CVD')

        # 4. Demência
        elif code_int in range(290, 291) or code.startswith('3312'):
            categorias.add('Dementia')

        # 5. Doença pulmonar crônica
        elif code_int in range(490, 496) or code.startswith('500') or code.startswith('5064') or code.startswith('5181'):
            categorias.add('COPD')

        # 6. Doença reumática
        elif code.startswith('714') or code.startswith('7100') or code.startswith('7101') or code.startswith('7104'):
            categorias.add('Rheum')

        # 7. Úlceras pépticas
        elif code.startswith('531') or code.startswith('532') or code.startswith('533') or code.startswith('534'):
            categorias.add('PUD')

        # 8. Doença hepática leve
        elif code.startswith('5712') or code.startswith('5714') or code.startswith('5715') or code.startswith('5716'):
            categorias.add('MildLiver')

        # 9. Diabetes (sem complicação)
        elif code.startswith('2500') or code.startswith('2501') or code.startswith('2502') or code.startswith('2503'):
            categorias.add('Diabetes')

        elif code.startswith('2500') or code.startswith('2501') or code.startswith('2502') or code.startswith('2503'):
            categorias.add('Diabetes')

        # 10. Diabetes com complicações
        elif code.startswith('2504') or code.startswith('2505') or code.startswith('2506') or code.startswith('2507') or code.startswith('2508') or code.startswith('2509'):
            categorias.add('DiabComp')

        # 11. Hemiplegia/paraplegia
        elif code.startswith('342') or code.startswith('343') or code.startswith('3441'):
            categorias.add('Paralysis')

        # 12. Doença renal crônica
        elif code.startswith('582') or code.startswith('5830') or code.startswith('585') or code.startswith('586') or code.startswith('5880'):
            categorias.add('Renal')

        # 13. Câncer (exceto metástase)
        elif code_int in range(140, 173) or code_int in range(174, 176) or code_int in range(179, 195) or code_int in range(200, 209):
            categorias.add('Cancer')

        # 14. Câncer metastático
        elif code.startswith('196') or code.startswith('197') or code.startswith('198') or code.startswith('199'):
            categorias.add('Mets')

        # 15. Doença hepática grave
        elif code.startswith('5722') or code.startswith('5723') or code.startswith('5724') or code.startswith('5728'):
            categorias.add('SevLiver')

        # 16. HIV/AIDS
        elif code.startswith('042') or code.startswith('043') or code.startswith('044'):
            categorias.add('HIV')

    return categorias

pesos_charlson = {
    'CHF': 1,
    'PVD': 1,
    'CVD': 1,
    'Dementia': 1,
    'COPD': 1,
    'Rheum': 1,
    'PUD': 1,
    'MildLiver': 1,
    'Diabetes': 1,
    'DiabComp': 2,
    'Paralysis': 2,
    'Renal': 2,
    'Cancer': 2,
    'Mets': 6,
    'SevLiver': 3,
    'HIV': 6
}

def calcular_cci(categorias):
    return sum(pesos_charlson.get(cat, 0) for cat in categorias)

def pontos_idade(idade):
    if idade < 50:
        return 0
    elif idade < 60:
        return 1
    elif idade < 70:
        return 2
    elif idade < 80:
        return 3
    elif idade < 90:
        return 4
    else:
        return 5