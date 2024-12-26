package com.example.pos.moodle;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PosMoodleController {

    @GetMapping("/")
    public String hello() {
        return "Hello World";
    }
}
