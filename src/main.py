# import pyperclip

chord_name = "B"
fret_shift = None
chord_input = "[1-6]1"

def parse_pair(pair: str):
    parsed_pair = []
    for s in pair:
        if s.isdigit():
            parsed_pair.append(int(s))
        else:
            parsed_pair.append(s)
    return parsed_pair
            
def root(pair: list):
    root_base = f"\\color{{red}}"
    if len(pair) > 2 and pair[2] == "r":
        return root_base
    else:
        return ""

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
        # calculate barre position and length
        barre_length = 2.25*(barre_input_end - barre_input_start + 1)-0.25
        barre_shift = -0.875*(barre_input_end - barre_input_start + 1)+1.025
        barre_length = f'{barre_length:.2f}'
        barre_shift = f'{barre_shift:.2f}'

    # single frets
    frets_input = [pair for pair in chord_input if "-" not in pair and "x" not in pair and "0" not in pair]
    frets_input = [parse_pair(pair) for pair in frets_input]

    line_base = "{}&{}&{}&{}&{}"
    
    dot_base = "{{}}\\llap{{${}\\raisebox{{-0.15em}}{{$\\large{{\\bull}}\\kern{{0.05em}}$}}$}}"
    barre_base = "{{}}\\llap{{$\\rule[0pt]{{{}ex}}{{1ex}}\\kern{{{}em}}$}} "


    # how many frets to draw
    if len(frets_input) == 0:
        max_fret = 0
    else:
        max_fret = max([pair[1] for pair in frets_input])
    if len(barre_input) > 0:
        max_fret = max(max_fret, barre_input_fret)

    fret_draw = max(max_fret, 3) # draw at least 3 frets

    fret_shift_raise = f'{0.5*fret_draw-0.5:.2f}'
    marker_raise = f"{0.5*fret_draw+0.5:.2f}"

    # open strings markers
    open_strings_input = [parse_pair(pair) for pair in chord_input if "x" in pair or "0" in pair]
    open_string_pieces = "\\raisebox{{{}}}{{${}\\sixptsize{{{}}}\\kern{{{}em}}$}}"
    chord_open_strings = []

    # draw open strings markers
    for pair in open_strings_input:
        if pair[1] == "x":
            marker = "×"
        elif pair[1] == 0:
            marker = "○"
        else:
            marker = " "
        open_string_marker_shift = 1.65*pair[0]-10.9
        open_string_marker_shift = f'{open_string_marker_shift:.2f}'
        chord_open_strings.append(open_string_pieces.format(f"{marker_raise}em", root(pair), marker, open_string_marker_shift))

    chord_open_strings = "".join(chord_open_strings)

    lines = []
    for fret in range(1, fret_draw+1): # for eath fret (row)
        line_tail = "\\\\ \\hline" if fret != fret_draw else ""
        pieces = ["" for _ in range(7)]
        # draw barre
        if len(barre_input) > 0 and barre_input_fret == fret:
            # calculate barre position and length
            pieces[barre_input_end] = barre_base.format(barre_length, barre_shift) 

        # draw single frets
        for fret_input in frets_input: # for each fret input
            # dealing with single notes
            if fret_input[1] == fret:
                if fret_input[0] != 1:
                    pieces[fret_input[0]] += dot_base.format(root(fret_input)) 
                elif fret_input[0] == 1: # string 1 - need to use string 2
                    pieces[2] += "{{}}\\llap{{${}\\raisebox{{-0.15em}}{{$\\large{{\\bull}}$\\kern{{-0.9em}}}}$}}".format(root(fret_input))
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
    
    # print(chord)
    # pyperclip.copy(chord)
    return chord

if __name__ == "__main__":
    gen_katex_chord(chord_name, fret_shift, chord_input)