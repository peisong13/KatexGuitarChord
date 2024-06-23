import * as React from 'react';

import GenerateButton from './GenerateButton';
import ClearButton from './ClearButton';

import { Stack } from '@mui/material';

const Buttons = (props) => {
    return (
        <Stack direction="row" spacing={2} sx={{ padding: "10px 10px 50px 10px"}}>
            <GenerateButton 
                inputChordName={props.inputChordName} 
                inputFretShift={props.inputFretShift} 
                inputChordNotes={props.inputChordNotes} 
                inputCopyToClipboard={props.inputCopyToClipboard}
                outputKatex={props.outputKatex} 
                setOutputKatex={props.setOutputKatex}/>
            <ClearButton clearInputTextField={props.clearInputTextField}/>
        </Stack>
    )
}

export default Buttons;