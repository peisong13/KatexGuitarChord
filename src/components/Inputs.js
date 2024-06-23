import { Checkbox, FormControlLabel, TextField } from '@mui/material';
import * as React from 'react';
import Stack from '@mui/material/Stack';

const Inputs = ( props ) => {
    return (
        <Stack spacing={2} direction='column' padding="80px 10px 40px 10px" margin={0}> 
            <Stack direction='row' spacing={2}>
            <TextField id="chord-name" label="Chord Name" variant="outlined" size="small" sx={{ flex: 2 }}
                value={props.inputChordName} onChange={(e)=>props.setInputChordName(e.target.value)}/>
            <TextField id="fret-shift" label="Fret Shift" variant="outlined" size="small" sx={{ flex: 1 }}
                value={props.inputFretShift} onChange={(e)=>props.setInputFretShift(e.target.value)}/>
            </Stack>
            <TextField id="chord-notes" label="Chord Notes" variant="outlined" size="small"
                value={props.inputChordNotes} onChange={(e)=>props.setInputChordNotes(e.target.value)}/>
            <FormControlLabel control={<Checkbox checked={props.inputCopyToClipboard} onChange={(e)=>props.setInputCopyToClipboard(e.target.checked)}/>} label="Copy to Clipboard"/>
            
        </Stack>
    )
}

export default Inputs;