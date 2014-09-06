var problem_3 = function() {
    var c = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736';

    raw_c = hexToRaw(c);

    var xor_byte = breakSingleByteXOR(raw_c);
    $('#problem_3 ul').append($('<li>').text(xor_byte));

    var result = xorRawSingleChar(raw_c, String.fromCharCode(xor_byte));
    $('#problem_3 ul').append($('<li>').text(result));
}