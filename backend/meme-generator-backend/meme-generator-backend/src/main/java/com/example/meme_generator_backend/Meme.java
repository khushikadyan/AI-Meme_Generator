package com.example.meme_generator_backend;

public class Meme {
    private String name;
    private String base_img;  // Change this to match the JSON property
    private int textBox;

    // Constructor
    public Meme(String name, String base_img, int textBox) {
        this.name = name;
        this.base_img = base_img;
        this.textBox = textBox;
    }

    // Getters and Setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getBase_img() {  // Update getter
        return base_img;
    }

    public void setBase_img(String base_img) {  // Update setter
        this.base_img = base_img;
    }

    public int getTextBox() {
        return textBox;
    }

    public void setTextBox(int textBox) {
        this.textBox = textBox;
    }
}