import pyperclip

chord_name = "Ab13"
fret_shift = None
chord_input = "64 5x 44 33 [1-2]1"

def gen_katex_chord(chord_name, fret_shift, chord_input):
    chord_input = chord_input.split(" ")
    fret_shift = 0 if not fret_shift else int(fret_shift)
    fret_shift = fret_shift if fret_shift != 0 else " "

    # replace # and b
    bf_base = "\\raisebox{{0.1em}}{{${}$}}"
    if "#" in chord_name:
        chord_name = chord_name.replace("#", bf_base.format("\\sharp"))
    elif "b" in chord_name:
        chord_name = chord_name.replace("b", bf_base.format("\\flat"))

    # examine barre
    barre_input = [pair for pair in chord_input if "-" in pair]
    if len(barre_input) > 0:
        barre_input = barre_input[0]
        barre_input_start, barre_input_end, barre_input_fret = int(barre_input[1]), int(barre_input[3]), int(barre_input[5])
        # swap barre_start and barre_end if barre_start > barre_end
        if barre_input_start > barre_input_end:
            barre_input_start, barre_input_end = barre_input_end, barre_input_start
        # calculate barrer position and length
        barrer_length = 2.25*(barre_input_end - barre_input_start + 1)-0.25
        barrer_shift = -0.875*(barre_input_end - barre_input_start + 1)+1.025
        barrer_length = f'{barrer_length:.2f}'
        barrer_shift = f'{barrer_shift:.2f}'

    # root note
    root_note_input = [pair for pair in chord_input if 'r' in pair]
    if len(root_note_input) > 0:
        root_note_input = root_note_input[0] # TODO: draw root note

    # single frets
    frets_input = [pair for pair in chord_input if "-" not in pair and "x" not in pair and "0" not in pair and "r" not in pair]
    frets_input = [[int(pair[0]), int(pair[1])] for pair in frets_input]

    line_base = "{}&{}&{}&{}&{}"
    root = ""
    dot_base = "{{{}}}\\llap{{$\\raisebox{{-0.15em}}{{$\\large{{\\bull}}\\kern{{0.05em}}$}}$}}"
    barrer_base = "{{{}}}\\llap{{$\\rule[0pt]{{{}ex}}{{1ex}}\\kern{{{}em}}$}} "



    # how many frets to draw
    max_fret = max([pair[1] for pair in frets_input])
    if len(barre_input) > 0:
        max_fret = max(max_fret, barre_input_fret)

    fret_draw = max(max_fret, 3)

    fret_shift_raise = f'{0.5*fret_draw-0.5:.2f}'
    marker_raise = f"{0.5*fret_draw+0.5:.2f}"

    # open strings markers
    open_strings_input = [[int(pair[0]), pair[1]] for pair in chord_input if "x" in pair or "0" in pair]
    open_string_pieces = "\\raisebox{{{}}}{{$\\sixptsize{{{}}}\\kern{{{}em}}$}}"
    chord_open_strings = []

    for pair in open_strings_input:
        if pair[1] == "x":
            marker = "×"
        elif pair[1] == "0":
            marker = "○"
        else:
            marker = " "
        open_string_marker_shift = 1.65*pair[0]-10.9
        open_string_marker_shift = f'{open_string_marker_shift:.2f}'
        chord_open_strings.append(open_string_pieces.format(f"{marker_raise}em", marker, open_string_marker_shift))

    chord_open_strings = "".join(chord_open_strings)

    lines = []
    for fret in range(1, fret_draw+1): # for eath fret (row)
        line_tail = "\\\\ \\hline" if fret != fret_draw else ""
        pieces = ["" for _ in range(7)]
        if len(barre_input) > 0 and barre_input_fret == fret:
            # calculate barrer position and length
            pieces[barre_input_end] = barrer_base.format(root, barrer_length, barrer_shift) 
        for fret_input in frets_input: # for each fret input
            # dealing with single notes
            if fret_input[1] == fret:
                if fret_input[0] != 1:
                    pieces[fret_input[0]] += dot_base.format(root) 
                elif fret_input[0] == 1: # string 1 - need to use string 2
                    pieces[2] += "{{{}}}\\llap{{$\\raisebox{{-0.15em}}{{$\\large{{\\bull}}$\\kern{{-0.9em}}}}$}}".format(root)
        lines.append(line_base.format(pieces[6], pieces[5], pieces[4], pieces[3], pieces[2]) + line_tail)

    lines[-1] = lines[-1].replace(line_tail, "") # 最后一行不需要封闭线

    # body
    chord_body = "\n".join(lines)

    chord = f"""\\scriptsize{{\\def\\arraystretch{{1}}
    \\begin{{array}}{{c}}
    \\enspace \\small{{{chord_name}}} \\\\ 
    \\raisebox{{{fret_shift_raise}em}}{{$\\scriptsize{{\\mathsf{{{fret_shift}}}}}$}} {chord_open_strings} \\enspace

    \\begin{{array}}{{|c|c|c|c|c|}}
        \\hline 
        {chord_body}
    \\end{{array}}
    \\end{{array}}}}
    """
    
    print(chord)
    pyperclip.copy(chord)
    return chord

if __name__ == "__main__":
    gen_katex_chord(chord_name, fret_shift, chord_input)