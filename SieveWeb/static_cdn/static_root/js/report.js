function myFunction(value) {
    if (value === "census1971") {
        document.getElementById("image").style.display='none';
        document.getElementById("Dglow1").style.display = 'block';
        document.getElementById("Dglow2").style.display = 'none';
        document.getElementById("Dglow3").style.display = 'none';
        document.getElementById("Dglow4").style.display = 'none';
        document.getElementById("Dglow5").style.display = 'none';
    }
     else if (value === "census1981") {
        document.getElementById("image").style.display='none';
        document.getElementById("Dglow1").style.display = 'none';
        document.getElementById("Dglow2").style.display = 'block';
        document.getElementById("Dglow3").style.display = 'none';
        document.getElementById("Dglow4").style.display = 'none';
        document.getElementById("Dglow5").style.display = 'none';
    }
     else if (value === "census1991") {
        document.getElementById("image").style.display='none';
        document.getElementById("Dglow1").style.display = 'none';
        document.getElementById("Dglow2").style.display = 'none';
        document.getElementById("Dglow3").style.display = 'block';
        document.getElementById("Dglow4").style.display = 'none';
        document.getElementById("Dglow5").style.display = 'none';
    }

    else if (value === "census2001") {
        document.getElementById("image").style.display='none';
        document.getElementById("Dglow1").style.display = 'none';
        document.getElementById("Dglow2").style.display = 'none';
        document.getElementById("Dglow3").style.display = 'none';
        document.getElementById("Dglow4").style.display = 'block';
        document.getElementById("Dglow5").style.display = 'none';
    }
    else if (value === "census2011") {
        document.getElementById("image").style.display='none';
        document.getElementById("Dglow1").style.display = 'none';
        document.getElementById("Dglow2").style.display = 'none';
        document.getElementById("Dglow3").style.display = 'none';
        document.getElementById("Dglow4").style.display = 'none';
        document.getElementById("Dglow5").style.display = 'block';
    }
};
