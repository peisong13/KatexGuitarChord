document.getElementById('submitBtn').addEventListener('click', function() {
    var latexInput = document.getElementById('latexInput').value;
    var chordShiftInput = document.getElementById('chordShiftInput').value
    var chordName = document.getElementById('chordNameInput').value

    pywebview.api.gen_katex_chord_api(chordName, chordShiftInput, latexInput).then(function(latexChord) {
        var latexOutput = document.getElementById('latexOutput');
        latexOutput.innerHTML = katex.renderToString(latexChord, {
            throwOnError: false
        });
    }
    ).catch(function(error) {
        console.error("API Error:", error);
    });

    function catchException() {
        pywebview.api.error().catch(function(err) {
            console.error("Error in API call:", err);
        });
    }
});
