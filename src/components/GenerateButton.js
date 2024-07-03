import { Box, Button } from '@mui/material';
import * as React from 'react';

const GenerateButton = ( props ) => {
    const { inputChordName, inputFretShift, inputChordNotes, inputCopyToClipboard, outputKatex, setOutputKatex } = props;
    const generateChord = () => {
        (window).pywebview.api.gen_katex_chord_api(inputChordName, inputFretShift, inputChordNotes).then(function(latexChord) {
            var latexOutput = document.getElementById('katex-render');
            setOutputKatex(latexChord);
            latexOutput.innerHTML = (window).katex.renderToString(latexChord, {
                throwOnError: false
            });
            // copy katex to clipboard
            if (inputCopyToClipboard) {
                (window).pywebview.api.copy_to_clipboard_api(latexChord).then(()=>{})
            }
        }
        ).catch(function(error) {
            console.error("API Error:", error);
        });
        
    }

    return (
        <Box spacing={2} flex={1}>
            <Button id="generate" variant="contained" sx={{ textTransform: 'none', width: "100%", m:'1px'}} onClick={()=>{ generateChord() }} >Generate</Button>
        </Box>
        
    )
}

export default GenerateButton;