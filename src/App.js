import { Divider, Stack } from '@mui/material';
import './App.css';
import MainAppBar from './components/Appbar'
import Inputs from './components/Inputs';
import Outputs from './components/Outputs';
import Box from '@mui/material/Box';
import Buttons from './components/Buttons';
import * as React from 'react';

function App() {
  const [inputChordName, setInputChordName] = React.useState('');
  const [inputFretShift, setInputFretShift] = React.useState('');
  const [inputChordNotes, setInputChordNotes] = React.useState('');
  const [inputCopyToClipboard, setInputCopyToClipboard] = React.useState(true);
  const [outputKatex, setOutputKatex] = React.useState(' ');

  const clearInputTextField = ( ) => {
      setInputChordName("")
      setInputChordNotes("")
      setInputFretShift("")
  }

  return (
    <Box className="App" padding="0px" margin="0px">
      <div className="pywebview-drag-region"><MainAppBar /></div>
      <Stack className="AppBody" direction='row' padding="2px 10px 0px 10px" divider={<Divider orientation="vertical" flexItem />} justifyContent='space-between'>
        <Stack direction="column" spacing={2} padding="10px 0px 10px 0px" sx={{ flex: 1 }}>
          <Inputs
           inputChordName={inputChordName}
           setInputChordName={setInputChordName}
           inputFretShift={inputFretShift}
           setInputFretShift={setInputFretShift}
           inputChordNotes={inputChordNotes}
           setInputChordNotes={setInputChordNotes}
           inputCopyToClipboard={inputCopyToClipboard}
           setInputCopyToClipboard={setInputCopyToClipboard}
          />
          <Buttons clearInputTextField={clearInputTextField} padding="10px 0px 0px 0px"
            inputChordName={inputChordName}
            inputFretShift={inputFretShift} 
            inputChordNotes={inputChordNotes} 
            inputCopyToClipboard={inputCopyToClipboard} 
            outputKatex={outputKatex} 
            setOutputKatex={setOutputKatex}/>
        </Stack>
          <Outputs sx={{ flex: 1 }} outputKatex={outputKatex} setOutputKatex={setOutputKatex}/>
      </Stack>
    </Box>

  );
}

export default App;
