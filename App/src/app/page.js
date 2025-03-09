"use client"

import { useState, useEffect, use } from "react";
import { GoogleGenerativeAI } from "@google/generative-ai";
import { Bar, BarChart } from "recharts"
import { ChartConfig, ChartContainer } from "@/components/ui/chart"
import axios from 'axios';
import "./globals.css"
import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"
 
import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Textarea } from "@/components/ui/textarea"
import { Backpack } from "lucide-react";
 
const FormSchema = z.object({
  text: z
    .string()
    .min(10, {
      message: "Bio must be at least 10 characters.",
    })
    .max(160, {
      message: "Bio must not be longer than 30 characters.",
    }),
})

export default function Home() {

  
  const form = useForm()
    // const form = useForm<z.infer<typeof FormSchema>>({ resolver: zodResolver(FormSchema), })

  const key = process.env.NEXT_PUBLIC_API_KEY;
  const genAI = new GoogleGenerativeAI(key);
  const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });
  const prePrompt = 'Only respond with json formatted keywords (use the format - {"keywords":["your-words-here"]}) that you would expect be in a mission statement of a related charity each word should be specific to the type of charity derived from the following passage: ';
  let preResult = ''
  const [aiResponse, setAiResponse] = useState(null); 
  const [pResult, setPResult] = useState(null);
  // const [preResult, setPreResult] = useState(null); 

  
  async function onSubmit(data) {
      prompt = prePrompt + data.text;

      try {
          preResult = await model.generateContent(prompt);
          
      } catch (error) {
          alert("Error generating AI response:", error);
          console.log("Error generating AI response:", error);
      }

      axios
        .post("http://localhost:4000/api", JSON.parse(preResult.response.text().substring(8, preResult.response.text().length - 4)))
        .then((response) => setAiResponse(response))
        .catch((error) => console.error(error));
  }

  const chartConfig = {
    desktop: {
      label: "Desktop",
      color: "#2563eb",
    },
  }

  let parsedArray1
  let parsedArray2
  let half1;
  let half2;
  let chartData = [];
  if (aiResponse) {
    const arrayStr = aiResponse.data.substring(8, aiResponse.data.length - 2)
    console.log(arrayStr)

    const validJsonString1 = arrayStr.replace(/'/g, '"');
    parsedArray1 = JSON.parse(validJsonString1);
    chartData = parsedArray1.map(item => ({
        year: parseInt(item[0]), 
        desktop: parseFloat(item[1]) 
    }));
  }


  const cd = chartData
  // console.log(ch)

  return (
    <>
      <div className="mb-10">
        <h1 className="text-center text-3xl font-bold py-5 bg-white"
          style={{boxShadow: "0px 2px 8px 0px rgba(60, 64, 67, 0.25)", border: "1px solid rgb(234, 221, 220)"}}
        >
          Lorem Ipsum Title</h1>

          <img className="h-[60dvh] w-full object-cover absolute z-[-10]" src="https://media.licdn.com/dms/image/v2/C4D12AQGhNtX_9mAdbg/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1581786335388?e=2147483647&v=beta&t=ZF2-Nfcl5rNYfpMGJMINx1jBETlsEXDc6oJf0hyqqZw"></img>
          
          <div className="flex h-[60dvh] items-center justify-center  flex-wrap">
            <div>
              <div className="mx-10  my-10 w-[2xl] flex flex-column justify-center items-center h-[200px] bg-[rgba(255,255,255,0.8)] px-5 rounded-md">
                  <Form {...form}>
                    <form onSubmit={form.handleSubmit(onSubmit)} className="w-2xl space-y-6">
                      <FormField
                        control={form.control}
                        name="text"
                        render={({ field }) => (
                          <FormItem>
                            <FormLabel><strong>What kind of Charity are you interested in?</strong></FormLabel>
                            <FormControl>
                              <Textarea
                                placeholder="Tell us a little bit about the charity"
                                className="resize-none"
                                {...field}
                                style={{border: "1px solid gray"}}
                              />
                            </FormControl>
                            <FormDescription>
                              Ex: water conservation
                            </FormDescription>
                            <FormMessage />
                          </FormItem>
                        )}
                      />
                      <Button type="submit">Submit</Button>
                    </form>
                  </Form>
              </div>
            </div>

            <div className="h-[200px] overflow-scroll p-[20px] bg-white rounded-md"
                style={{boxShadow: "0px 2px 8px 0px rgba(60, 64, 67, 0.25)", border: "1px solid rgb(234, 221, 220)"}}
            >
                <ul>
                  <li>Tech Innovations Inc. - $5.8 Billion</li>
                  <li>Global Solutions Ltd. - $3.2 Billion</li>
                  <li>Eco Industries Group - $1.5 Billion</li>
                  <li>Health Care Partners Co. - $2.9 Billion</li>
                  <li>Creative Digital Enterprises - $4.3 Billion</li>
                  <li>Future Vision Technologies - $7.6 Billion</li>
                  <li>Premier Manufacturing Corp. - $6.1 Billion</li>
                  <li>Green Energy Solutions - $800 Million</li>
                  <li>Skyline Investments Group - $9.4 Billion</li>
                  <li>NextGen Robotics - $2.2 Billion</li>
                  <li>Tech Innovations Inc. - $5.8 Billion</li>
                  <li>Global Solutions Ltd. - $3.2 Billion</li>
                  <li>Eco Industries Group - $1.5 Billion</li>
                  <li>Health Care Partners Co. - $2.9 Billion</li>
                  <li>Creative Digital Enterprises - $4.3 Billion</li>
                  <li>Future Vision Technologies - $7.6 Billion</li>
                  <li>Premier Manufacturing Corp. - $6.1 Billion</li>
                  <li>Green Energy Solutions - $800 Million</li>
                  <li>Skyline Investments Group - $9.4 Billion</li>
                  <li>NextGen Robotics - $2.2 Billion</li>
                </ul>
            </div>
          </div>
                  
          <div className="w-full flex justify-center mt-10">
            <div className="flex px-[150px] justify-center my-10">
                <div className="mx-10 px-10 text-lg rounded-md mb-10 w-100"
                    style={{boxShadow: "0px 2px 8px 0px rgba(60, 64, 67, 0.25)", border: "1px solid rgb(234, 221, 220)"}}
                    >
                    <h1 className="text-xl font-bold pt-[15px] text-center"
                      style={{borderBottom: "2px solid rgba(60, 64, 67, 0.25)"}}
                    >
                      Legend</h1>
                    <p className="py-5">This is the general predicted trend line of other popular charities similar to the description you provided</p>
                    {/* <ul> */}
                      {/* <li>Canser Research</li>
                      <li>Water conservation</li>
                      <li>Green Energy</li> */}
                    {/* </ul> */}
                </div>

                <ChartContainer config={chartConfig} className="min-h-[200px] mb-[15px] w-full pb-10">
                  <BarChart accessibilityLayer data={cd}>
                    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
                  </BarChart>
                </ChartContainer>
            </div>
          </div>
          
      </div>

      
    </>
  );
}

