import { Box, Divider, TextField } from '@mui/material';
import * as React from 'react';
import Stack from '@mui/material/Stack';
import KatexOutputRender from './KatexOutputRender';

const Outputs = (props) => {
    const { outputKatex, setOutputKatex } = props;
    return (
        <Box flex={1} sx={{ margin: "20px" }}>
            <Stack direction="column" divider={<Divider orientation="horizontal" flexItem />} spacing={2} sx={{ blockSize: "100px"}} justifyContent='space-around'>
                <TextField id="Katex-output" multiline value={outputKatex} label="Katex Output" maxRows={7} variant="outlined" sx={{
                    '& .MuiOutlinedInput-root': {
                    height: '180px',
                    alignItems: 'flex-start', // 将文本内容顶部对齐
                    },
                    '& .MuiOutlinedInput-input': {
                    height: '100%',
                    boxSizing: 'border-box',
                    caretColor: 'initial', // 使用默认光标颜色
                    },
                }}  />
                <KatexOutputRender />
            </Stack>
        </Box>
        
        
    )
}

export default Outputs;