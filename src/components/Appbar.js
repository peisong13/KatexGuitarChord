import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import { Box } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import MinimizeIcon from '@mui/icons-material/Minimize';

const MainAppBar = () => {
    return (
            <AppBar position="sticky" >
                <Toolbar variant='dense' sx={{ minHeight:'10px', justifyContent:"space-around"}}>
                    <Typography variant='body2' component="div" sx={{ fontSize: '0.8rem', flex: 15, textAlign: "start"}}>
                        Katex Guitar Chord
                    </Typography>
                    <Button 
                        color='inherit'
                        onClick={()=>{window.pywebview.api.minimize_window()}}
                        sx={{ transform: 'scale(0.8)', minWidth: 'auto', transformOrigin: 'center center', padding: '1px', flex: 1}}><MinimizeIcon /></Button>
                    <Button 
                        color="inherit" 
                        onClick={()=>{window.pywebview.api.close_window()}}
                        sx={{ transform: 'scale(0.8)', minWidth: 'auto', transformOrigin: 'center center', padding: '1px', flex: 1}}><CloseIcon /></Button>
                </Toolbar>


            </AppBar>

    );
    
}
export default MainAppBar;