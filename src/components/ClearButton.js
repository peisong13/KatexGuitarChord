import { Box, Button } from '@mui/material';
import * as React from 'react';

const ClearButton = (props) => {
    return (
        <Box spacing={2} flex={1}>
            <Button variant="outlined" sx={{ textTransform: 'none', width: "100%", m:'1px'}} onClick={()=>{props.clearInputTextField()}}>Clear</Button>
        </Box>
        
    )
}

export default ClearButton;