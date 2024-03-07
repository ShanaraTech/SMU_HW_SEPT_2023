
function dropdown(){

// Get the data using the URL in line 2
d3.json("https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json").then(function(data) {
    console.log(data);

// Use D3 to select the dropdown
    let dropdown = d3.select("#selDataset");

// populate the dropdown
    for (let i = 0; i < data.names.length; i++){
        let name = data.names[i];
        dropdown.append("option").text(name);
    }

// Extract necessary data fields
   let individual = data.names[0];
    console.log(individual);
    charts(individual)

    table(individual)
})
}
function optionChanged(individual){
    charts(individual)
    table(individual)
}
function table(individual){
    d3.json("https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json").then(function(data) {
        console.log(data);

        let metadata = data.metadata;
        let resultArray = metadata.filter(row => row.id == individual);
        let result = resultArray[0];

// Use D3 to select the dropdown for metadata
let dropdownMetadata = d3.select("#sample-metadata");

dropdownMetadata.html("");
// Prints "name Jean-Luc Picard" followed by "rank Captain"
Object.entries(result).forEach(entry => {
    const [key, value] = entry;
    console.log(key, value);
    dropdownMetadata.append("h6")
    .text(`${key}: ${value}`);

  });
})
}


function charts(individual){
    d3.json("https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json").then(function(data) {
        console.log(data);

   let samples = data.samples;
   let resultArray = samples.filter(row => row.id == individual);
   let result = resultArray[0];

   let sample_values = result.sample_values;
   let otu_ids = result.otu_ids;
   let otu_labels = result.otu_labels;

// Sort the data to get the top 10 OTUs
   let top10Values = sample_values.slice(0, 10);
   let top10Ids = otu_ids.slice(0, 10);
   let top10Labels = otu_labels.slice(0, 10);


// Create a horizontal bar chart using Plotly
    let trace = {
       x: top10Values,
       y: top10Ids.map(id => `OTU ${id}`),
       text: top10Labels,
       type: "bar",
       orientation: "h",
       marker: {
            color: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], // Assign a numerical value to each bar for the color scale
            colorscale: "Picnic", // Choose a color scale (e.g., Viridis, Plasma, etc.)
            reversescale: true, // This line flips the color scale
            colorbar: {
                title: "Color Scale"
            }
       }
    };

   let bar_data = [trace];

   let layout = {
       title: "Top 10 OTUs in Human Navels",
       xaxis: { title: "Sample Values" },
       yaxis: { title: "Individual OTU IDs" }
   };

Plotly.newPlot("bar",bar_data, layout);

// Create a bubble chart using Plotly
    let trace2 = {
        x: otu_ids,
        y: sample_values,
        text: otu_labels,
        type: "scatter",
        mode: "markers",
        marker: {
            size: sample_values,
            color: otu_ids,
            colorscale: "Picnic"
        }
    };

    let bubble_data = [trace2];

// Layout options for the bubble chart
    let bubble_layout = {
        xaxis: {
            title: "OTU IDs"
        },
        yaxis: {
            title: "Sample Values",
            anchor: "x",
            position: 0.1
        },
        margin: {
            l: 100,
            r: 100,
            t: 100,
            b: 100
        }
    };
        
// Create the bubble chart using Plotly
Plotly.newPlot("bubble", bubble_data, bubble_layout);
});
}
dropdown()
