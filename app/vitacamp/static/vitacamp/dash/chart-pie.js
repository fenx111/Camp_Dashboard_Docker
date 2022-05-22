Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Спортивные", "Творческие", "Учебные"],
    datasets: [{
      data: [55, 30, 15],
      backgroundColor: ['rgba(78, 115, 223, 0.6)', 'rgba(28, 200, 138, 0.6)', 'rgba(54, 185, 204, 0.6)'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgba(0,0,0, 0.7)",
      bodyFontColor: "#f2f3f7",
      bodyFontSize: 14,
      titleMarginBottom: 10,
      titleFontColor: '#f2f3f7',
      titleFontSize: 16,
      // backgroundColor: "rgb(255,255,255)",
      // bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 0,
  },
});
