package de.colenet.romannumerals;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class RomanNumeralsTest {
    @Test
    void arabic_1_is_converted_to_I() {
        var actual = RomanNumeralsConverter.convert(1);
        Assertions.assertEquals("I", actual);
    }
}
