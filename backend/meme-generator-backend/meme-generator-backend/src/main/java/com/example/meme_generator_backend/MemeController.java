package com.example.meme_generator_backend;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.Arrays;
import java.util.List;

@RestController
@RequestMapping("/api")
public class MemeController {

    @Autowired
    private RestTemplate restTemplate;

    @PostMapping("/suggest-memes")
    public List<Meme> suggestMemes(@RequestBody MemeRequest request) {
        String flaskApiUrl = "http://127.0.0.1:5000/suggest-memes";  // Flask server URL
        MemeRequest memeRequest = new MemeRequest();
        memeRequest.setIdea(request.getIdea());

        // Make a request to Flask API
        Meme[] memes = restTemplate.postForObject(flaskApiUrl, memeRequest, Meme[].class);

        return Arrays.asList(memes);  // Return memes received from Flask API
    }

    static class MemeRequest {
        private String idea;

        public String getIdea() {
            return idea;
        }

        public void setIdea(String idea) {
            this.idea = idea;
        }
    }
}
